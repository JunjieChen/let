import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.core.*;
import weka.core.converters.ConverterUtils.DataSource;

public class Classify_1 {
	public static void main(String[] args) throws Exception
	{

        DataSource atf2 = new DataSource("feature_filter_selected.csv");
        Instances instancesTest = atf2.getDataSet(); 
      
        instancesTest.setClassIndex(instancesTest.numAttributes() - 1);
        System.out.println(instancesTest.numAttributes() - 1);
        //load the trained classifier
        Classifier classifier5 = (Classifier) weka.core.SerializationHelper.read("SMO.model");
        
        BufferedWriter writer = new BufferedWriter(new FileWriter("probability.txt", true));
        
        BufferedReader reader = new BufferedReader(new FileReader("fileorder_filter.txt"));
        
        for(int i = 0; i < instancesTest.numInstances(); i++)
        {
        	writer.write(reader.readLine() + " = ");
        	writer.write(classifier5.distributionForInstance(instancesTest.instance(i))[0] + "\n");
        }
        writer.close();

	}
}
