import tensorflow as tf
import tensorflow.python.platform

IMAGE_SIZE = 28
NUM_CLASSES = 2
# AIの学習モデル部分(ニューラルネットワーク)を作成する
# images_placeholder: 画像のplaceholder, keep_prob: dropout率のplace_holderが引数になり
# 入力画像に対して、各ラベルの確率を出力して返す
def inference(images_placeholder, keep_prob):
  # 重みを標準偏差0.1の正規分布で初期化する
  def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

  # バイアスを標準偏差0.1の正規分布で初期化する
  def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

  # 畳み込み層を作成する
  def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

  # プーリング層を作成する
  def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')
  # ベクトル形式で入力されてきた画像データを28px * 28pxの画像に戻す(?)。

  # 今回はカラー画像なので3(モノクロだと1)
  x_image = tf.reshape(images_placeholder, [-1, IMAGE_SIZE, IMAGE_SIZE, 3])

  # 畳み込み層第1レイヤーを作成
  with tf.name_scope('conv1') as scope:
    # 引数は[width, height, input, filters]。
    # 5px*5pxの範囲で画像をフィルターしている。今回はカラー画像なのでinputは3?
    # 32個の特徴を検出する
    W_conv1 = weight_variable([5, 5, 3, 32])

    # バイアスの数値を代入
    b_conv1 = bias_variable([32])

    # 特徴として検出した有用そうな部分は残し、特徴として使えなさそうな部分は
    # 0として、特徴として扱わないようにしているという理解(Relu関数)
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)

  # プーリング層1の作成
  # 2*2の枠を作り、その枠内の特徴を1*1分にいい感じに圧縮させている。
  # その枠を2*2ずつスライドさせて画像全体に対して圧縮作業を適用するという理解
  # ざっくり理解で細分化された特徴たちをもうちょっといい感じに大まかにまとめる(圧縮する)
  with tf.name_scope('pool1') as scope:
    h_pool1 = max_pool_2x2(h_conv1)

  # 畳み込み層第2レイヤーの作成
  with tf.name_scope('conv2') as scope:
    # 第一レイヤーでの出力を第2レイヤー入力にしてもう一度フィルタリング実施。
    # 64個の特徴を検出する。inputが32なのはなんで?(教えて欲しい)
    W_conv2 = weight_variable([5, 5, 32, 64])

    # バイアスの数値を代入(第一レイヤーと同じ)
    b_conv2 = bias_variable([64])

    # 検出した特徴の整理(第一レイヤーと同じ)
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)

  # プーリング層2の作成(ブーリング層1と同じ)
  with tf.name_scope('pool2') as scope:
    h_pool2 = max_pool_2x2(h_conv2)

  # 全結合層1の作成
  with tf.name_scope('fc1') as scope:
    W_fc1 = weight_variable([7*7*64, 1024])
    b_fc1 = bias_variable([1024])
    # 画像の解析を結果をベクトルへ変換
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])

    # 第一、第二と同じく、検出した特徴を活性化させている
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    # dropoutの設定
    # 訓練用データだけに最適化して、実際にあまり使えないような
    # AIになってしまう「過学習」を防止の役割を果たすらしい
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

  # 全結合層2の作成(読み出しレイヤー)
  with tf.name_scope('fc2') as scope:
    W_fc2 = weight_variable([1024, NUM_CLASSES])
    b_fc2 = bias_variable([NUM_CLASSES])

  # ソフトマックス関数による正規化
  # ここまでのニューラルネットワークの出力を各ラベルの確率へ変換する
  with tf.name_scope('softmax') as scope:
    y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

  # 各ラベルの確率(のようなもの?)を返す
  return y_conv

# 予測結果と正解にどれくらい「誤差」があったかを算出する
# logitsは計算結果:  float - [batch_size, NUM_CLASSES]
# labelsは正解ラベル: int32 - [batch_size, NUM_CLASSES]
def loss(logits, labels):
  # 交差エントロピーの計算
  cross_entropy = -tf.reduce_sum(labels*tf.log(logits))

  # TensorBoardで表示するよう指定
  tf.summary.scalar("cross_entropy", cross_entropy)

  # 誤差の率の値(cross_entropy)を返す
  return cross_entropy

# 誤差(loss)を元に誤差逆伝播を用いて設計した学習モデルを訓練する
# 裏側何が起きているのかよくわかってないが、学習モデルの各層の重み(w)などを
# 誤差を元に最適化して調整しているという理解(?)
# (誤差逆伝播は「人工知能は人間を超えるか」書籍の説明が神)
def training(loss, learning_rate):
  #この関数がその当たりの全てをやってくれる様
  train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss)
  return train_step

# inferenceで学習モデルが出した予測結果の正解率を算出する
def accuracy(logits, labels):
  # 予測ラベルと正解ラベルが等しいか比べる。同じ値であればTrueが返される
  # argmaxは配列の中で一番値の大きい箇所のindex(=一番正解だと思われるラベルの番号)を返す
  correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))

  # booleanのcorrect_predictionをfloatに直して正解率の算出
  # false:0,true:1に変換して計算する
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

  # TensorBoardで表示する様設定
  tf.summary.scalar("accuracy", accuracy)
  return accuracy
