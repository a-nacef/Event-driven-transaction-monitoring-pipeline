package singleton;

public class Test {

	/*
	 * Client
	 */
	public static void main(String[] args) {
		
		Config c1 = Config.getInstance();
		Config c2 = Config.getInstance();
		
		if(c1 == c2) {
			System.out.println("smae");
		}
	}

}
