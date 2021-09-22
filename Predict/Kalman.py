from pykalman import KalmanFilter


class KalmanP:
    def __init__(self):
        self.code = 'mimaz.org'

    def Kalman(self, observations, damping=1):
        observation_covariance = damping
        initial_value_guess = observations[0]
        transition_matrix = 1
        transition_covariance = 0.1
        kf = KalmanFilter(initial_state_mean=initial_value_guess,
                          initial_state_covariance=observation_covariance,
                          observation_covariance=observation_covariance,
                          transition_covariance=transition_covariance,
                          transition_matrices=transition_matrix)
        pred_state, state_cov = kf.smooth(observations)
        return pred_state, state_cov