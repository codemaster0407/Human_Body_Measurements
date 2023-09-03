import numpy as np

def estimate_transformation_matrix_3D(points_2D, points_3D):
    # Convert to homogeneous coordinates
    points_2D_homogeneous = np.hstack((points_2D, np.ones((len(points_2D), 1))))
    points_3D_homogeneous = np.hstack((points_3D, np.ones((len(points_3D), 1))))

    # Normalization
    points_2D_normalized, T_2D = normalize_points(points_2D_homogeneous)
    points_3D_normalized, T_3D = normalize_points(points_3D_homogeneous)

    # Construct the linear system
    A = []
    for i in range(len(points_2D_normalized)):
        x, y, w = points_2D_normalized[i]
        X, Y, Z, _ = points_3D_normalized[i]
        A.append([-X, -Y, -Z, -1, 0, 0, 0, 0, x*X, x*Y, x*Z, x])
        A.append([0, 0, 0, 0, -X, -Y, -Z, -1, y*X, y*Y, y*Z, y])
    A = np.array(A)

    # Perform Singular Value Decomposition (SVD)
    _, _, V = np.linalg.svd(A)

    # Compute the transformation matrix
    H = V[-1, :].reshape(3, 4)
    H = np.linalg.inv(T_2D) @ H @ np.linalg.inv(T_3D)

    return H


def normalize_points(points):
    centroid = np.mean(points[:, :2], axis=0)
    std_dev = np.std(points[:, :2])
    scale_factor = np.sqrt(2) / std_dev

    T = np.array([[scale_factor, 0, -scale_factor * centroid[0]],
                  [0, scale_factor, -scale_factor * centroid[1]],
                  [0, 0, 1]])

    normalized_points = points @ T.T

    return normalized_points, T




# Example usage
points_2D = np.array([[0, 0], [1, 2], [3, 4]])  # 2D image coordinates
points_3D = np.array([[0, 0, 1], [1, 2, 4], [3, 4, 7]])  # 3D coordinates

transformation_matrix = estimate_transformation_matrix_3D(points_2D, points_3D)
print(transformation_matrix)
