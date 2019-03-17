def body_force(dest):
    for i in range(len(dest.x)):
        dest.fy[i] = dest.m[i] * -9.81
        dest.fx[i] = 0.


def interparticle_force(d_x, d_y, d_fx, d_fy, d_rad, s_x, s_y, s_rad, kn):
    for i in range(len(d_x)):
        for j in range(len(s_x)):
            # check for the overlap
            dx = d_x[i] - s_x[j]
            dy = d_y[i] - s_y[j]
            rij = (dx**2 + dy**2)**(0.5)
            if rij > 1e-13:
                overlap = d_rad[i] + s_rad[j] - rij
                nx = dx / rij
                ny = dy / rij

                if overlap > 0.:
                    d_fx[i] += kn * overlap * nx
                    d_fy[i] += kn * overlap * ny


def soil_step(dest, dt):
    for i in range(len(dest.x)):
        dest.u[i] += dest.fx[i] / dest.m[i] * dt
        dest.v[i] += dest.fy[i] / dest.m[i] * dt

        dest.x[i] += dest.u[i] * dt
        dest.y[i] += dest.v[i] * dt
