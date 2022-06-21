package facory.factory;

import factory.model.BMW;
import factory.model.M_BMW;
import factory.model.Moteur;
import factory.model.VHC;

public class BMW_Factory extends AbstractFactory {

	@Override
	public VHC creerVHC() {
		Moteur mbmw = new M_BMW();
		/*.....*/
		VHC v = new BMW(mbmw);
		return v;
	}

}
