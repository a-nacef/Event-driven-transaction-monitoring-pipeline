package composite;

public class Tache implements Composant {
	private int duree;
	private int nbEmp;
	private double cout;
	
	public Tache() {
		// TODO Auto-generated constructor stub
	}
	public Tache(int duree, int nbEmp, double cout) {
		super();
		this.duree = duree;
		this.nbEmp = nbEmp;
		this.cout = cout;
	}	
	
	public int getNbEmp() {
		return nbEmp;
	}

	public void setNbEmp(int nbEmp) {
		this.nbEmp = nbEmp;
	}

	public void setDuree(int duree) {
		this.duree = duree;
	}

	public void setCout(double cout) {
		this.cout = cout;
	}

	@Override
	public int getDuree() {
		return duree;
	}

	@Override
	public double getCout() {
		return duree*nbEmp*cout;
	}

}
