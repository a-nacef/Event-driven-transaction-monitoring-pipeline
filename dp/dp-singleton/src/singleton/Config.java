package singleton;

public class Config {
	
	private  static Config instance; 
	
	private Config() {
		// TODO Auto-generated constructor stub
	}
	
	public synchronized static Config getInstance(){
		if(instance == null) {
			instance =  new Config();
		}
		return instance;
	}
	
	

}
