import weka.classifiers.Classifier;
import weka.classifiers.functions.GaussianProcesses;
import weka.classifiers.functions.SMO;
import weka.core.Instances;
import weka.core.SerializationHelper;
import weka.core.converters.ConverterUtils.DataSource;


public class Trainingset {
	public static void main(String[] args) throws Exception
	{
		DataSource source = null;     
        	Instances instancesTrain = null; 
		source = new DataSource("yes_1000_no_1000_times_selected.csv");  
		instancesTrain = source.getDataSet();    
		instancesTrain.setClassIndex(instancesTrain.numAttributes()-1);  

        Classifier classifier1 = null;
        
        classifier1 = new SMO();
    	classifier1.setOptions(weka.core.Utils.splitOptions("-C 1.0 -L 0.0010 -P 1.0E-12 -N 0 -M -V -1 -W 1 -K \" weka.classifiers.functions.supportVector.Puk -C 250007 -O "+args[0]+" -S "+args[1]+"\""));//1.2 0.7 
    	
    	classifier1.buildClassifier(instancesTrain);
    	
    	//save the trained classifier
        SerializationHelper.write("SMO.model", classifier1);
		
}
}
