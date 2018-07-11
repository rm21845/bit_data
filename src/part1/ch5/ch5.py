import pandas as pd
from matplotlib import pyplot as plt
import sklearn.datasets as ds
from pandas.tools.plotting import scatter_matrix
import statsmodels.api as sm
import urllib
import numpy as np

class ch5():
    def get_iris_df(self): 
        """Basis for charts"""
        print('Snippet 1')
        data_s = ds.load_iris()
        df = pd.DataFrame(data_s['data'],
                          columns = data_s['feature_names'])
        code_species_map = dict(zip(
            range(3), data_s['target_names']))
        df['species'] = [code_species_map[c]
                         for c in data_s['target']]
        return df

    def two_a(self,df):
        """Pie chart 1"""
        print('Snippet 2a')
        sums_by_species = df.groupby('species').sum()
        var = 'sepal width (cm)'
        sums_by_species[var].plot(kind='pie', fontsize=20)
        plt.ylabel(var, horizontalalignment='left')
        plt.title('Breakdown for ' + var, fontsize=35)
        plt.savefig('iris_pie_for_one_variable.jpg')
        plt.close()

    def two_b(self,df):
        """Pie chart 2"""
        print('Snippet 2b')
        sums_by_species = df.groupby('species').sum()
        sums_by_species.plot(kind='pie', subplots=True,
                             layout=(2,2), legend=False)
        plt.title('Total Measurements, by Species')
        plt.savefig('iris_pie_for_each_variable.jpg')
        plt.close()

    def three(self,df):
        """Bar chart"""
        print('Snippet 3')
        sums_by_species = df.groupby('species').sum()
        var = 'sepal width (cm)'
        sums_by_species[var].plot(kind='bar', fontsize=15,
                                  rot=30)
        plt.title('Breakdown for ' + var, fontsize=20)
        plt.savefig('iris_bar_for_one_variable.jpg')
        plt.close()
        sums_by_species = df.groupby('species').sum()
        sums_by_species.plot(
            kind='bar', subplots=True, fontsize=12)
        plt.suptitle('Total Measurements, by Species')
        plt.savefig('iris_bar_for_each_variable.jpg')
        plt.close()

    def four(self, df):
        """Histogram"""
        print('Snippet 4')
        df.plot(kind='hist', subplots=True, layout=(2,2))
        plt.suptitle('Iris Histograms', fontsize=20)
        plt.show()
        plt.close()

        for spec in df['species'].unique():
            forspec = df[df['species']==spec]
            forspec['petal length (cm)'].plot(
                kind='hist', alpha=0.4, label=spec)

        plt.legend(loc='upper right')
        plt.suptitle('Petal Length by Species')
        plt.savefig('iris_hist_by_spec.jpg')

    def five(self, df):
        """Mean, Median, Standard Deviation, and Quantiles"""
        print('Snippet 5')
        col = df['petal length (cm)']
        Average = col.mean()
        Std = col.std()
        Median = col.quantile(0.5)
        Percentile25 = col.quantile(0.25)
        Percentile75 = col.quantile(0.75)
       # print('Column: ' + col)
       # print('Average: ' + Average)
       # print('Standard Deviation: ' + Std)
       # print('Median: ' + Median)
       # print('25th Percentile: ' + Percentile25)
       # print('75th Percentile: ' + Percentile75)

        print('Removing outliers...')
        col = df['petal length (cm)']
        Perc25 = col.quantile(0.25)
        Perc75 = col.quantile(0.75)
        Clean_Avg = col[(col>Perc25)&(col<Perc75)].mean()
       # print('Column: ' + col + '25th %: ' + Perc75 + '75th %: ' +
        #      Perc75 + 'Clean Average: ' + Clean_Avg)

    def six(self, df):
        """Boxplots"""
        print('Snippet 6')
        col = 'sepal length (cm)'
        df['ind'] = pd.Series(df.index).apply(lambda i: i% 50)
        df.plot('ind','species') [col].plot(kind='box')
        plt.show()

    def seven(self, df):
        """Scatterplots"""
        print('Snippet 7')
        df.plot(kind='scatter',
                x='sepal length (cm)', y='sepal width (cm)')
        plt.title('Length vs Width')
        plt.show()
        plt.close()

        colors = ['r', 'g', 'b']
        markers = ['.', '*', '^']
        fig, ax = plt.subplots(1,1)
        for i, spec in enumerate(df['species'].unique()):
            ddf = df[df['species']==spec]
            ddf.plot(kind='scatter',
                x='sepal width (cm)', y='sepal length (cm)',
                alpha=0.5, s=10* (i+1), ax=ax,
                color=colors[i], marker=markers[i], label=spec)
            plt.legend()
            plt.show()

    def eight(self, df):
        """"scatter w/ logarithmic Axes"""
        print('Snippet 8')
        #make Pandas dataframe
        bs = ds.load_boston()
        df = pd.DataFrame(bs.data, columns=bs.feature_names)
        df['MEDV'] =bs.target
        #Normal Scatterplot
        df.plot(x='CRIM', y='MEDV', kind='scatter')
        plt.title('Crime rate on normal axis')
        plt.show()

        #Make x-axis logarithmic
        df.plot(x='CRIM', y='MEDV', kind='scatter', logx=True)
        plt.title('Crime rate on logarithmic axis')
        plt.show()
        plt.close()

    def nine(self, df):
        """Scatter Matrices"""
        print('Snippet 9')
        scatter_matrix(df)
        plt.show()
        plt.close()

    def ten(self, df):
        """Heatmaps"""
        print('Snippet 10')
        df.plot(kind='hexbin',
            x='sepal width (cm)', y='sepal length (cm)')
        plt.show()

    def eleven(self, df):
        """Correlations"""
        print('Snippet 11')
        print(df['sepal width (cm)'].corr( #Pearson corr
            df['sepal length (cm)']))

        print(df['sepal width (cm)'].corr( 
            df['sepal length (cm)'], method='pearson'))

        print(df['sepal width (cm)'].corr( 
            df['sepal length (cm)'], method='spearman'))

        print(df['sepal width (cm)'].corr( 
            df['sepal length (cm)'], method='spearman'))

    def twelve(self, df):
        """Time Series"""
        print('Snippet 12')
        dta = sm.datasets.co2.load_pandas().data
        dta.plot()
        plt.title('CO2 Levels')
        plt.ylabel('Parts per million')
        plt.show()

        #Get raw CSV data from the web
        URL = ('http://ichart.finance.yahoo.com/' +
               'table.csv?s=GOOG&c=2000')
       # dat = urllib.request.urlopen(URL).read()
       # open('foo.csv', 'w').write(dat)
        #Make Dataframe, w timestamp as the index
       # df = pd.read_csv('foo.csv')
      #  df.index = df['Date'].astype('datetime64')
      #  df['LogClose'] = np.log(df['Close'])
      #  df['Close'].plot()
      #  plt.title('Normal Axis')
      #  plt.show()
      #  df['Close'].plot(logy=True)
      #  plt.title('Logarithmic axis')
      #  plt.show()

    def main(self):
        print('Chapter 5 Results')
        df = self.get_iris_df()
        self.two_a(df)
        self.two_b(df)
        self.three(df)
        self.four(df)
        self.five(df)
        self.seven(df)
        self.eight(df)
        self.nine(df)
        self.ten(df)
        self.eleven(df)
        self.twelve(df)
