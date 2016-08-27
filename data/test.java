import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.core.*;
import weka.core.converters.ConverterUtils.DataSource;

public class test {
	public static void main(String[] args) throws Exception
	{

        DataSource atf2 = new DataSource("feature_filter_testtime.csv");
        Instances instancesTest = atf2.getDataSet();
      
        instancesTest.setClassIndex(instancesTest.numAttributes() - 1);//////////////////////////////////////
        System.out.println(instancesTest.numAttributes() - 1);
        //load the trained classifier
        Classifier classifier5 = (Classifier) weka.core.SerializationHelper.read("Gaussian.model");
        
        BufferedWriter writer = new BufferedWriter(new FileWriter("predictedtime.txt"));
        
        BufferedReader reader = new BufferedReader(new FileReader("fileorder_filter.txt"));
        
        for(int i = 0; i < instancesTest.numInstances(); i++)
        {
        	writer.write(reader.readLine() + " = ");
        	writer.write(classifier5.classifyInstance(instancesTest.instance(i)) + "\n");
        }
        writer.close();

	}
}
