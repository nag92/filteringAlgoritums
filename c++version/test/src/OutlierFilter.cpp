#include "OutlierFilter.h"
#include <random>
#include <ctime>


OutlierFilter::OutlierFilter(void)
{
}

OutlierFilter::OutlierFilter(int mySize, double confid, int myWindow, int* range)
{
	size = mySize;
	window = myWindow;

	data = new BLAS::matrix<double>(size,window);
	mdList = new BLAS::matrix<double>(1,window);
	confinence = sqrt(confid);

	//for generating random numbers
	srand(time(NULL));
	double randNum = 0;

	//fill list with random numbers
	for(int i = 0; i < size; i++)
	{
		for(int j = 0; j< window;j++)
		{
			randNum = ((range[1] - range[0])*( (double)rand() / RAND_MAX) + range[0]);
			data->insert_element(i,j, randNum);

			randNum = ((range[1] - range[0])*( (double)rand() / RAND_MAX) + range[0]);
			mdList->insert_element(0,j,randNum);
		}
	}
}

bool OutlierFilter::isGood(BLAS::vector<double>& points)
{
	static int count = 0;
	bool isGood= false;
	double mdMean = 0;
	double mdDeviation = 0;

	BLAS::vector<double> distance(1);//hold the md
	BLAS::matrix<double>* updated(data);//new list to hold all the obervations
	BLAS::matrix<double> diff(data->size1(),data->size2());//holds the differance between the obervations and the mean
	BLAS::matrix<double>* transposed(data);//holds transpose of the differance
	BLAS::matrix<double>* cov;//holds the covariance of the data
	BLAS::matrix<double> inverse(data->size1(), data->size1());//hold the inverase of the covariance
	BLAS::matrix<double> diffInverse1,diffInverse2;//holds parts "md" eq
	BLAS::vector<double> row;//holds a the row of a matrix to pass it to the mean
	BLAS::matrix<double> col(updated->size1(),1);//hold the last column of the observations
	BLAS::vector<double> mean(size);//hold the mean of each row in the list

	//add in the new points
	updated = popMatrix(*data, points);
	data = updated;

	//get the mean of each row
	for (unsigned int i = 0; i< updated->size1(); i++)
	{
		row = BLAS::row(*updated,i);
		mean(i) = getMean(row);
	}

	//subtract the row mean from each point
	for( unsigned int i = 0; i < diff.size1(); i++)
	{
		for( unsigned int j = 0; j< diff.size2();j++)
		{
			diff.insert_element(i,j, updated->at_element(i,j) - mean(i));
		}
	}

	//get and inverse the covaraince matrix
	cov =  getCovariance(*updated,mean) ;//return heap memory
	rfalInverse(*cov, inverse);

	//get the last column of the data (most recent point)
	BLAS::column(col,0) = BLAS::column(diff,diff.size2()-1);

	//get the transpose of the point
	transposed = new BLAS::matrix<double>(BLAS::trans(col));

	//calculate the mahalanobis distance and add it to list
	diffInverse1 = BLAS::prod(*transposed,inverse);
	diffInverse2 = BLAS::prod(diffInverse1,col);
	distance.insert_element(0,sqrt(diffInverse2(0,0)));

	//see if all the random values are out of the list
	if(count < window)
	{
		count++;
		//add the new md to the list
		mdList = popMatrix(*mdList, distance);
		//set wieghting idx
	}

	//get the mean and standard deviation of the mdList
	//extract the row
	row = BLAS::row(*mdList,0);
	mdMean = getMean(row);
	//std = sqrt( variance )
	mdDeviation = sqrt( getVariance(row,mdMean,row,mdMean));

	//threshold test to see if the point is an outlier
	if( distance(0) < confinence)
	{
		isGood = true;
		//if the point is good and all the random data is gone then add the new point to the list
		if(count > window)
		{
			mdList = popMatrix(*mdList, distance);
		}
	}

	//clean up
	delete cov;
	std::cout<<"mdList "<<*mdList<<std::endl;
	std::cout<<"data "<<*data<<std::endl;
	return isGood;
}

//get the mean of the list
double OutlierFilter::getMean(BLAS::vector<double>& list)
{
	double sum = 0;

	for(unsigned int i = 0; i<list.size();i++)
		sum+=list(i);

	return sum/window;
}

//add a new element to the row and removes the oldest point in each row (push each row)
BLAS::matrix<double>* OutlierFilter::popMatrix(BLAS::matrix<double>& list, BLAS::vector<double>& points)
{
	BLAS::matrix<double>* newList(&list);

	for(unsigned int i = 0; i< list.size1(); i++)
	{
		for(unsigned int j = 0; j < list.size2() - 1; j++)
		{
			//shift the elements in the list
			newList->at_element(i,j) = list.at_element(i,j+1);
		}

		newList->at_element(i,newList->size2()-1) = points(i);
	}

	return newList;
}
//calculate the Covariance of a matrix
//pass combinations of vectors in to the variance fucntion and use it to build the covariance matrix
BLAS::matrix<double>* OutlierFilter::getCovariance(BLAS::matrix<double>& data, BLAS::vector<double>& means )
{
	BLAS::matrix<double> temp( data.size1(),data.size1());
	BLAS::matrix<double>* cov = new BLAS::matrix<double>(data.size1(),data.size1());
	BLAS::vector<double> observation1;//holds a the row of a matrix to pass it to the mean
	BLAS::vector<double> observation2;

	for(unsigned int i = 0; i < cov->size1(); i++)
	{
		observation1 = BLAS::row(data,i);
		for( unsigned int j = 0; j < cov->size1(); j++)
		{
			observation2 = BLAS::row(data,j);
			cov->insert_element(i,j , getVariance(observation1,means(i), observation2,means(j) ));
		}
	}

	return cov;
}

//calculate the variance of two vectors(co-variance)
//if both vectors are the same then it is the variance
double OutlierFilter::getVariance(BLAS::vector<double>& list1,double mean1,BLAS::vector<double>& list2,double mean2)
{
	double sum = 0;

	for(unsigned int i = 0; i < list1.size(); i++)
	{
		sum += (list1(i) - mean1)*(list2(i) - mean2);
	}

	return sum/(list1.size()-1);
}

//inverse of a matrix
template<class T>
bool OutlierFilter::rfalInverse( const BLAS::matrix<T>& input , BLAS::matrix<T>& inverse )
{
  // create a working copy of the input
  BLAS::matrix<T> A( input );

  // create a permutation matrix for the LU-factorization
  BLAS::permutation_matrix<std::size_t> pm( A.size1( ) );

  // perform LU-factorization
  int res = BLAS::lu_factorize( A , pm );

  if( res != 0  )
    return false;

  // create identity matrix of "inverse"
  inverse.assign( BLAS::identity_matrix<T>( A.size1( ) ) );

  // backsubstitute to get the inverse

  BLAS::lu_substitute( A , pm , inverse );

  return true;

}

OutlierFilter::~OutlierFilter(void)
{
}
