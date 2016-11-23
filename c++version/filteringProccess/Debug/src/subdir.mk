################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/MDFilter.cpp \
../src/OutlierFilter.cpp \
../src/kalman.cpp \
../src/main.cpp 

OBJS += \
./src/MDFilter.o \
./src/OutlierFilter.o \
./src/kalman.o \
./src/main.o 

CPP_DEPS += \
./src/MDFilter.d \
./src/OutlierFilter.d \
./src/kalman.d \
./src/main.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: Cross G++ Compiler'
	g++ -I/usr/include -O0 -g3 -Wall -c -fmessage-length=0,-std=c++11 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


