import java.io.BufferedWriter;
import java.io.FileWriter;

import weka.attributeSelection.ASEvaluation;
import weka.attributeSelection.ASSearch;
import weka.attributeSelection.AttributeSelection;
import weka.attributeSelection.GainRatioAttributeEval;
import weka.attributeSelection.Ranker;
import weka.core.Instances;
import weka.core.converters.ConverterUtils.DataSource;


public class FeatureSelection {
	public static void main(String[] args) throws Exception
	{
		
		DataSource source = null;     
        Instances instancesTrain = null; 
		source = new DataSource("yes_800_no_800_times_4.csv");  
		instancesTrain = source.getDataSet();    
		instancesTrain.setClassIndex(instancesTrain.numAttributes()-1);  
		
		ASEvaluation evaluator = new GainRatioAttributeEval();
		ASSearch search = new Ranker();
		AttributeSelection eval = null;
		
		eval = new AttributeSelection();
		eval.setEvaluator(evaluator);
		eval.setSearch(search);
		eval.SelectAttributes(instancesTrain);
		
		BufferedWriter writer = new BufferedWriter(new FileWriter("selected.txt", true));
		
		double[][] selectedAttributes = eval.rankedAttributes();
		for(int i=0;i<instancesTrain.numAttributes()-1;i++){
			if(selectedAttributes[i][1] > 0){
				writer.write((int)(selectedAttributes[i][0])+",");
			}
		}
		
		writer.close();
	}
}
