
import weka.classifiers.Classifier;
import weka.classifiers.functions.*;
import weka.core.Instances;
import weka.core.SerializationHelper;
import weka.core.converters.ConverterUtils.DataSource;

public class train {

		public static void main(String[] args) throws Exception
		{
			DataSource source = null;
	       		Instances instancesTrain = null;
			source = new DataSource("time_trainingset.csv");
			instancesTrain = source.getDataSet();
			instancesTrain.setClassIndex(instancesTrain.numAttributes()-1);

            Classifier classifier1 = null;

            classifier1 = new GaussianProcesses();
        	classifier1.setOptions(weka.core.Utils.splitOptions("-L 1.0 -N 0 -K \"weka.classifiers.functions.supportVector.Puk -C 250007 -O "+args[0]+" -S "+args[1]+"\""));//2.5,1.6
        	//classifier1.setOptions(weka.core.Utils.splitOptions("-L 1.0 -N 0 -K \"weka.classifiers.functions.supportVector.RBFKernel -C 250007 -G 2.0\""));

        	classifier1.buildClassifier(instancesTrain);

        	//save the trained classifier
            SerializationHelper.write("Gaussian.model", classifier1);

	}

}

