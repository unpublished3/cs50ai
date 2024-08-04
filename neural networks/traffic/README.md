Testing on gtrsb-small dataset with three different signs. For a pait the first accuracy values are for testing set and the second for training set.

1.  Initially with only flattening and the output layer

         model.add(tf.keras.layers.Flatten())
         model.add(tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax"))

    Output:

         accuracy: 0.7083 - loss: 18.0029

2.  Next, convolution and max pooling was used

         # Convolution
         model.add(
         tf.keras.layers.Conv2D(
             32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
         ))

         # Pooling
         model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

    Output:

         accuracy: 0.8542 - loss: 2.9051

3.  A single dense layer with 128 nodes was added to the network

         model.add(tf.keras.layers.Dense(128, activation="relu"))

    Output:

         accuracy: 0.8839 - loss: 0.7248

         accuracy: 0.9193 - loss: 0.2824 (For training)

4.  The accuracy for testing data set compared to the training data-set was much lower so dropout was added

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

5.  Adding another dense layer with same paremeters as 3.

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

    The results are generally consistent for dropout of 0.5. However, other values of dropout still produce siginificantly different results.

6.  Two more dense layers were added but they made the model worse.

7.  Dropout was added to the second dense layer but the model became less accurate.

8.  Altering the no. of nodes of the second dense layer didn't improve the model

9.  Increasing the no. of nodes of the first dense layer from 128 to 1000 produced better results (dropout 0.5). 

    Output:

         Run-1:
          accuracy: 0.8929 - loss: 0.4122
          accuracy: 0.9434 - loss: 0.2216

         Run-2:
          accuracy: 0.8839 - loss: 1.0758
          accuracy: 0.9407 - loss: 0.2048

         Run-3:
          accuracy: 0.8810 - loss: 0.4926
          accuracy: 0.9587 - loss: 0.2130

10. Experimenting with other values of dropout

        (0.6) Consistent between runs
        accuracy: 0.9107 - loss: 0.4353
        accuracy: 0.9347 - loss: 0.2235

        (0.7) Consistent between runs
        accuracy: 0.8452 - loss: 1.0122
        accuracy: 0.9085 - loss: 0.3382

11. Since accuracy increased from 0.5 to 0.6 but dropped from 0.6 to 0.7 values between 0.6 and 0.7 were tested.  

12. 0.6 produced the most consisted and most accurate result. The accuracy for both testing and training set was over 90% so I consider the model fairly accurate and will stop here.