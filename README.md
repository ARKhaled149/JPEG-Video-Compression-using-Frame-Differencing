# JPEG-Video-Compression-using-Frame-Differencing
The project had 2 parts: encoding and decoding. In the encoding, the steps were:
•	Read the given video (demo44.mp4).
•	Convert the given video into sequence of frames.
•	Then, subtract each frame from its previous frame. (resulted frames are called residual frames)
•	Reference frames will remain as is (Reference frames will be frames 0,15,30,45 and 60)
•	Display the 5th and 10th residual frames
In the decoding part, the steps were:
•	Add frames to restore original frames back as shown in the figure above as an example.
•	Display the 5th and 10th restored images.
•	Now that you have the original frames back convert these sequence of frames into a video.
•	Write this video on your device so you can play it.

