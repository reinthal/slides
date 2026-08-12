"""Two-cluster probe direction illustration.

Red = False cluster, Blue = True cluster.
theta = probe direction imposed across the clusters (difference of means).
mu_minus / mu_plus = cluster centroids (centers of mass).
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

rng = np.random.default_rng(7)

# Shared tilted covariance so clusters look elongated/diagonal like the source.
tilt = np.deg2rad(18)             # small tilt off vertical
R = np.array([[np.cos(tilt), -np.sin(tilt)],
              [np.sin(tilt),  np.cos(tilt)]])
S = np.diag([0.30, 2.6])          # narrow x, long y  -> tall streaks
cov = R @ S @ R.T

n = 700
mu_false = np.array([-2.7, 0.2])   # red cluster center
mu_true = np.array([2.7, -0.2])    # blue cluster center

X_false = rng.multivariate_normal(mu_false, cov, n)
X_true = rng.multivariate_normal(mu_true, cov, n)

# Empirical centers of mass.
mu_minus = X_false.mean(axis=0)
mu_plus = X_true.mean(axis=0)

fig, ax = plt.subplots(figsize=(8, 6.6))
ax.set_facecolor("#c7cdd6")

ax.scatter(X_false[:, 0], X_false[:, 1], s=22, c="#d40000",
           edgecolors="none", alpha=0.85, label="False", zorder=2)
ax.scatter(X_true[:, 0], X_true[:, 1], s=22, c="#0a24d6",
           edgecolors="none", alpha=0.85, label="True", zorder=2)


def arrow(p0, p1, color, lw=2.6, ms=22):
    ax.add_patch(FancyArrowPatch(
        p0, p1, arrowstyle="-|>", mutation_scale=ms,
        lw=lw, color=color, shrinkA=0, shrinkB=0, zorder=5))


# Probe / direction theta: the vector across the two clusters (mu_plus - mu_minus).
arrow(mu_minus, mu_plus, "#111111", lw=3.0, ms=26)
mid = (mu_minus + mu_plus) / 2
d = mu_plus - mu_minus
ax.annotate(r"$\theta$", xy=mid + np.array([0.15, 0.55]),
            fontsize=26, fontweight="bold", color="#111111")

# Centroid markers.
for mu, txt, dx in [(mu_minus, r"$\mu^{-}$", -0.75), (mu_plus, r"$\mu^{+}$", 0.35)]:
    ax.scatter(*mu, s=260, marker="X", c="#f5d000",
               edgecolors="k", linewidths=1.8, zorder=6)
    ax.annotate(txt, xy=mu + np.array([dx, 0.55]),
                fontsize=24, fontweight="bold", color="k", zorder=7)

# Decision boundary: perpendicular bisector of the centroid segment.
n_hat = d / np.linalg.norm(d)
perp = np.array([-n_hat[1], n_hat[0]])
b0 = mid - perp * 6
b1 = mid + perp * 6
ax.plot([b0[0], b1[0]], [b0[1], b1[1]], "--", color="#b0006a",
        lw=2.2, zorder=4)

ax.set_xlim(-7, 7)
ax.set_ylim(-6.5, 6.5)
ax.set_xticks([]); ax.set_yticks([])
ax.grid(True, color="white", alpha=0.6, zorder=0)
ax.legend(loc="lower right", fontsize=15, framealpha=0.95, markerscale=1.6)

for s in ax.spines.values():
    s.set_edgecolor("#2a2a2a"); s.set_linewidth(3)

fig.patch.set_facecolor("#2a2a2a")
fig.tight_layout()
fig.savefig("probe_theta.png", dpi=150, facecolor=fig.get_facecolor())
print("wrote probe_theta.png")
