# JPEG-Video-Compression-using-Frame-Differencing
## The project had 2 parts: encoding and decoding. In the encoding, the steps were:
1. Read the given video (demo44.mp4).
2. Convert the given video into sequence of frames.
3. Then, subtract each frame from its previous frame. (resulted frames are called residual frames)
4. Reference frames will remain as is (Reference frames will be frames 0,15,30,45 and 60)
5. Display the 5th and 10th residual frames
## In the decoding part, the steps were:
1. Add frames to restore original frames back as shown in the figure above as an example.
2. Display the 5th and 10th restored images.
3. Now that you have the original frames back convert these sequence of frames into a video.
4. Write this video on your device so you can play it.

