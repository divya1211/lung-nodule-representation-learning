## Lung Nodule Representation Learning


### Learnings and thoughts

- The network is producing noise as output images.
- How to improve recontruction loss? Read literature. 
- Overfits for a single image using reconstruction loss and masked loss.

### Things done 

- [x] Converted data to 2D images wihtout mask
    - `180x180 px` 
    - Centered cropped on nodule
- [x] Dataloader for 2D lungs scans
- [x] Visualization for a single 2D lung scan
- [x] PyTorch model
    - Tilled `nxn` scan `I` into `mxm` blocks. Eg, `180x180` into 9 `60x60` blocks.
    - Used `Conv2D` as  _f_ to downsample blocks to `x_1, x_2, .., x_9`.
    - Use `X_\i` to predict `x_i`, where `x_pred_i` is the prediction.
      - Where `X_\i` is average pool of `x_1, x_2, ... x_i-1, x_i+1, ... x_n`.
    - `ConvTranspose2d` to upsample each `x_pred_i` to `I_pred_i`.
    - Combined all the predicted images blockes `I_pred_i` to `I_pred`
- [x] Loss function used is MSE Loss on `I_pred` and `I`.
- [x] Overfit a small batch of examples ~10 images. [Source](http://karpathy.github.io/2019/04/25/recipe/)
- [x] Try on zero input data.
- [x] Use more `Conv`, `DeConv`  layers. Used a smaller `fc` layer. 
- [x] Batchify the code for batchsize > 1 as stochastic gradient descent isn't happening.
- [x] Use only the re-construction loss on images for debugging.


### Rejected Ideas

- [x] Use small pre-trained models instead of `Conv`.
- [x] Run on MNIST

### Things to-do

- [ ] Explore different loss functions
- [ ] Plot distribution of the differences in v space
- [ ] Use BatchNorm 
- [ ] readme results write it down
- [ ] How do we check overfitting




