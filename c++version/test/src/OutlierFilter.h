/*
	Nathaniel Goldfarb
	9/9/15
	RFAL,Stevens Insitute of Tecnology

	A outlier filter using a rolling mahalanobis distance filter

*/


#pragma once
#include <boost/numeric/ublas/lu.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/numeric/ublas/matrix_proxy.hpp>
#include <boost/numeric/ublas/triangular.hpp>

#define BLAS boost::numeric::ublas

class OutlierFilter
{
	public:
		OutlierFilter(void);
		~OutlierFilter(void);
		OutlierFilter(int /*data size*/, double /*confidence*/, int /*window*/, int* /*range*/);
		bool isGood(BLAS::vector<double>&/*vector of new points*/);//returns true if it is not an outlier

	private:
		template<class T>
		bool rfalInverse( const BLAS::matrix<T>&/*matrix to invert*/ , BLAS::matrix<T>&/*holds the inverse*/ ) ;
		int size;//number of obervations
		int window;//data to keep track of
		double confinence;//how much is the data trusted
		BLAS::matrix<double>* mdList;//a list of pervous mahalanobis distance the size of window
		BLAS::matrix<double>* data;//keeps track of the data
		BLAS::matrix<double>* getCovariance(BLAS::matrix<double>&/*data*/,BLAS::vector<double>&/*means*/);
		BLAS::matrix<double>* popMatrix(BLAS::matrix<double>& list/*data*/, BLAS::vector<double>& points/*point to add*/);
		double getMean(BLAS::vector<double>&/*data to get mean of*/);
		double getVariance(BLAS::vector<double>&/* data set 1*/, double/*mean of data 2*/, BLAS::vector<double>&/*data set 2*/,double/*mean of data 2*/);

};
