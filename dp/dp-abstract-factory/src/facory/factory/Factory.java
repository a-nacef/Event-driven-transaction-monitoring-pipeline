package facory.factory;

import factory.model.BMW;
import factory.model.M_BMW;
import factory.model.Moteur;
import factory.model.VHC;

public class Factory {

	public VHC creerVhc(String type) {
		if(type.equals("BMW")) {
			Moteur mbmw = new M_BMW();
			/*.....*/
			VHC v = new BMW(mbmw);
			return v;
		}else if(type.equals("Ferrari")) {
			return null;
		}
		return null;
	}
}
