"""Select informative points on a purely mathematical assay response surface using a Gaussian-process surrogate."""
from kit import *
TITLE='Active Learning for a Fictional Assay'
LIVE=False

def kernel(x,y,length=.25):return np.exp(-np.sum((x[:,None]-y[None])**2,axis=2)/(2*length**2))
def posterior(x,y,query,noise=.01):
    k=kernel(x,x)+noise*np.eye(len(x));cross=kernel(x,query);mean=cross.T@np.linalg.solve(k,y);variance=np.maximum(1-np.sum(cross*np.linalg.solve(k,cross),axis=0),1e-12);return mean,variance
def objective(x):return np.sin(5*x[:,0])*np.cos(4*x[:,1])+.5*np.exp(-np.sum((x-.7)**2,axis=1)/.03)
def run(d,a):
    grid=np.linspace(0,1,18);xx,yy=np.meshgrid(grid,grid);candidates=np.column_stack([xx.ravel(),yy.ravel()]);truth=objective(candidates);rng=np.random.default_rng(a.seed);initial=rng.choice(len(truth),5,replace=False).tolist();chosen=initial.copy();curve=[]
    for _ in range(18):
        mean,var=posterior(candidates[chosen],truth[chosen],candidates);ucb=mean+1.5*np.sqrt(var);ucb[chosen]=-np.inf;chosen.append(int(np.argmax(ucb)));curve.append(float(truth[chosen].max()))
    remaining=[i for i in range(len(truth)) if i not in initial];random_ids=initial+rng.choice(remaining,18,replace=False).tolist()
    return dict(active_best=float(truth[chosen].max()),random_best=float(truth[random_ids].max()),grid_oracle_best=float(truth.max()),queries=len(chosen),initial_queries=5,scope='Dimensionless fictional response surface; no wet-lab parameters'),dict(candidates=candidates,true_response=truth,chosen_indices=np.array(chosen),best_so_far=np.array(curve))

if __name__=="__main__":main(run)
