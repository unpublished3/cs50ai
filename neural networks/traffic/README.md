Testing on gtrsb-small dataset with three different signs. For a pait the first accuracy values are for testing set and the second for training set.

1) Initially with only flattening and the output layer

        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax"))

    Output:

        accuracy: 0.7083 - loss: 18.0029

2) Next, convolution and max pooling was used

        # Convolution
        model.add(
        tf.keras.layers.Conv2D(
            32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ))

        # Pooling
        model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

    

    Output:

        accuracy: 0.8542 - loss: 2.9051

3) A single dense layer with 128 nodes was added to the network

        model.add(tf.keras.layers.Dense(128, activation="relu"))

    Output:

        accuracy: 0.8839 - loss: 0.7248

        accuracy: 0.9193 - loss: 0.2824 (For training)

4) The accuracy for testing data set compared to the training   data-set was much lower so dropout was added

        model.add(tf.keras.layers.Dropout(dropout_value))


    Dropout vs Accuracy

        (0.5)
        accuracy: 0.8482 - loss: 0.4082
        accuracy: 0.9026 - loss: 0.2099

        (0.25)
        accuracy: 0.8185 - loss: 0.4730
        accuracy: 0.7652 - loss: 0.4582

        (0.75)
        accuracy: 0.8304 - loss: 0.4971
        accuracy: 0.7091 - loss: 0.8065

    Other values of dropout not listed here were also test. The best result was produced by 0.5. However multiple runs of the same value of droput produced vastly different results. So, results from this model are insignificant.


5) Adding another dense layer with same paremeters as 3.

    Output:

        Run-1:
         accuracy: 0.8720 - loss: 0.4021
         accuracy: 0.8315 - loss: 0.4753 

        Run-2:
         accuracy: 0.8393 - loss: 0.4144
         accuracy: 0.8178 - loss: 0.5727 

        Run-3:
         accuracy: 0.8631 - loss: 0.6036
         accuracy: 0.8577 - loss: 0.3148 

    The results are generally consistent