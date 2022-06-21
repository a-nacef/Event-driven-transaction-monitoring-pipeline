package composite;

import java.util.ArrayList;
import java.util.List;

public class Projet implements Composant {
	private List<Composant> fils = new ArrayList<Composant>();
	
	public void add(Composant cp) {
		fils.add(cp);
	}
	
	public List<Composant> getFils(){
		return fils;
	}

	@Override
	public int getDuree() {
		int sommeDuree = 0;
		for(Composant cp : fils) {
			sommeDuree += cp.getDuree();
		}
		return sommeDuree;
	}

	@Override
	public double getCout() {
		double sommeCout = 0;
		for(Composant cp : fils) {
			sommeCout += cp.getCout();
		}
		return sommeCout;
	}

}
