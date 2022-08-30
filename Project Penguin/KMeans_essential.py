import numpy as np
import pandas as pd

def calc_sq_dist(X, K_means):
    """
    This function calculates the squared distance of a data point from
    any one of the centroids.
    """
    mat = []
    for x in X:
        sq_distances = []
        for centroid in K_means:
            sq_distances.append(calc_sq_distance_point(x, centroid))
        mat.append(np.array(sq_distances))
    return np.array(mat)

def calc_sq_distance_point(x, y):
    return np.sum((x - y) ** 2)

def determine_rank(sq_dist_mat):
    """
    Determines cluster assignment based on the squared distance from a centroid
    :param sq_dist_mat: squared distance
    :return:
    """
    m = np.argmin(sq_dist_mat, axis = 1)
    return np.eye(sq_dist_mat.shape[1])[m]

def reverse_rank_matrix(rank_matrix):
    rank_df = pd.DataFrame(rank_matrix, columns=range(rank_matrix.shape[1]))
    return rank_df.idxmax(axis=1)

def recalc_centroids(X, rank):
    """
    Re-calculate cluster centroids based on updated cluster assignment
    :param X:
    :param rank:
    :return:
    """
    return (np.divide(X.T.dot(rank), np.sum(rank, axis = 0))).T

def run_kmeans(data, k=2):
    row = np.shape(data)[0]
    col = np.shape(data)[1]
    kmeans = np.zeros((row, col))
    rank = np.zeros((row, k))
    random_inds = np.random.permutation(row)
    kmeans = data[random_inds[:k]]
    max_iteration = 1000
    for iter in range(max_iteration):
        sq_dist_mat = calc_sq_dist(data, kmeans)
        rank = determine_rank(sq_dist_mat)
        kmeans_old = kmeans
        kmeans = recalc_centroids(data, rank)
        if sum(abs(kmeans_old.flatten() - kmeans.flatten())) < 1e-6:
            break
    return kmeans, rank
    