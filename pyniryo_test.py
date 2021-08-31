from pyniryo import *

from pyniryo.vision import *
robot = NiryoRobot("192.168.1.146")
# observation_pose = PoseObject(
#     x=0.18, y=0.0, z=0.35,
#     roll=0.0, pitch=1.57, yaw=-0.2,
# )

# robot.calibrate_auto()

# robot.move_joints(0.2, -0.3, 0.1, 0.0, 0.5, -0.8)



# Getting image
robot.calibrate_auto()
# robot.close_connection()
# Getting calibration param
mtx, dist = robot.get_camera_intrinsics()
# # Moving to observation pose
# robot.move_pose(observation_pose)
while True:
    # Getting image
    img_compressed = robot.get_img_compressed()
    # Uncompressing image
    img_raw = uncompress_image(img_compressed)
    # Undistorting
    img_undistort = undistort_image(img_raw, mtx, dist)

    # - Display
    # Concatenating raw image and undistorted image
    concat_ims = concat_imgs((img_raw, img_undistort))

    # Showing images
    key = show_img("Images raw & undistorted", concat_ims, wait_ms=30)
    if key in [27, ord("q")]:  # Will break loop if the user press Escape or Q
        break
robot.close_connection()

