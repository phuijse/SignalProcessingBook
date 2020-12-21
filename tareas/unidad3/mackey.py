import numpy as np

def MackeyGlass(SNR=5., N=1000, n=10.0, tau=17., beta=0.2, gamma=0.1, dt=0.05, y0 = 0.9, rseed=0):
    T = 5
    t = np.linspace(0, T, num=N)
    N_full, tau_full = int(N*T/dt), int(tau/dt)
    ymg = y0*np.ones(shape=(N_full, ))
    # Runge-Kutta integration
    for i in range(tau_full, N_full-1):
        byd = beta*ymg[i-tau_full]/(1.0 + ymg[i-tau_full]**n)
        yk1 = dt*(-gamma*ymg[i] + byd)
        yk2 = dt*(-gamma*(ymg[i]+yk1/2) + byd)
        yk3 = dt*(-gamma*(ymg[i]+yk2/2) + byd)
        yk4 = dt*(-gamma*(ymg[i]+yk3) + byd)
        ymg[i+1] = ymg[i] + yk1/6 + yk2/3 +yk3/3 +yk4/6;
    ymg = ymg[::int(T/dt)]
    # Contaminación con ruido blanco aditivo
    s_noise = np.sqrt(np.var(ymg)/SNR) 
    np.random.seed(rseed)
    y_obs = ymg + s_noise*np.random.randn(len(ymg))
    return (t[:500], y_obs[:500]), (t[500:750], y_obs[500:750]), (t[750:], y_obs[750:])