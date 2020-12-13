#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import patches
# import pylab
import time
from math import cos, sin


class KalmanFilter:
    """
    Class to keep track of the estimate of the robots current state using the
    Kalman Filter
    """

    def __init__(self, markers):
        """
        Initialize all necessary components for Kalman Filter, using the
        markers (AprilTags) as the map
        Input:
        markers - an N by 4 array loaded from the parameters, with each element
            consisting of (x,y,theta,id) where x,y gives the 2D position of a
            marker/AprilTag, theta gives its orientation, and id gives its
            unique id to identify which one you are seeing at any given
            moment
        """
        # TODO: initialize these parameters
        self.markers = markers
        self.last_time = None  # Used to keep track of time between measurements
        self.Q_t = np.identity(2)
        self.R_t = np.identity(3)
        # x_t - [x, y, theta]
        self.x_t = np.zeros((3, 1))
        self.u_t = np.array([0., 0.])
        self.F = np.identity(3)
        self.P = 1000 * np.identity(3)
        self.H = np.identity(3)
        # dh/dx
        self.Jhx = np.identity(3)

    def prediction(self, v, imu_meas, dt):
        """
        Performs the prediction step on the state x_t and covariance P_t
        Inputs:
        v - a number representing in m/s the commanded speed of the robot
        imu_meas - a 5 by 1 numpy array consisting of the values
            (acc_x,acc_y,acc_z,omega,time), with the fourth of the values giving
            the gyroscope measurement for angular velocity (which you should
            use as ground truth) and time giving the current timestamp. Ignore
            the first three values (they are for the linear acceleration which
            we don't use)
        Outputs: a tuple with two elements
        predicted_state - a 3 by 1 numpy array of the prediction of the state
        predicted_covariance - a 3 by 3 numpy array of the prediction of the
            covariance
        """

        return

    def update(self, z_t):
        """
        Performs the update step on the state x_t and covariance P_t
        Inputs:
        z_t - an array of length N with elements that are 4 by 1 numpy arrays.
            Each element has the same form as the markers, (x,y,theta,id), with
            x,y gives the 2D position of the measurement with respect to the
            robot, theta the orientation of the marker with respect to the
            robot, and the unique id of the marker, which you can find the
            corresponding marker from your map
        Outputs:
        predicted_state - a 3 by 1 numpy array of the updated state
        predicted_covariance - a 3 by 3 numpy array of the updated covariance
        """
        if z_t is not None:
            # Transformation for AprilTag to get measured robot pose wrt world frame
            tag_pose_world = tag_pos(self.markers, z_t[3])
            # z - robot pose wrt world
            robot_pose_world = robot_pos(tag_pose_world, z_t[:3])
            # y = z - HX
            y = robot_pose_world - self.x_t
            # S
            S = np.dot(np.dot(self.Jhx, self.P), np.transpose(self.Jhx)) + self.R_t
            # Kalman gain
            K = np.dot(np.dot(self.P, self.Jhx), np.linalg.inv(S))
            # X = X + Ky
            self.x_t = self.x_t + np.dot(K, y)
            # P = (I - KH)P
            self.P = np.dot(np.eye(3) - np.dot(K, self.Jhx), self.P)
        return

    def step_filter(self, v, imu_meas, z_t):
        """
        Perform step in filter, called every iteration (on robot, at 60Hz)
        Inputs:
        v, imu_meas - descriptions in prediction. Will be None value if
            values are not available
        z_t - description in update. Will be None value if measurement is not
            available
        Outputs:
        x_t - current estimate of the state
        """
        # YOUR CODE HERE

        return self.x_t
