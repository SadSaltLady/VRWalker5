// Fill out your copyright notice in the Description page of Project Settings.


#include "DataTransmitter.h"

FString AddComma(FString Input)
{
	return Input + ", ";
}

FString ADataTransmitter::ParseIntoCSV(TArray<F_Data> Data)
{
	
	FString str = TEXT("");
	FString Temp = TEXT("");
	//Header for CSV
	str.Append(TEXT("Time, HeadPos, ControllerLeftPos, ControllerRIghtPos, AngularAcceleration, LinearAcceleration, AngularVelocity, LinearVelocity\n"));
	
	for (int i = 0; i < Data.Num(); i++)
	{
		F_Data Dat = Data[i];
		Temp = ""; 
		Temp.Append(AddComma(FString::SanitizeFloat(Dat.Time)));
		Temp.Append(AddComma(Dat.HeadPos.ToString()));
		Temp.Append(AddComma(Dat.ControllerLeftPos.ToString()));
		Temp.Append(AddComma(Dat.ControllerRightPos.ToString()));
		Temp.Append(AddComma(Dat.AngularAcceleration.ToString()));
		Temp.Append(AddComma(Dat.LinearAcceleration.ToString()));
		Temp.Append(AddComma(Dat.AngularVelocity.ToString()));
		Temp.Append(Dat.LinearVelocity.ToString() + "\n");
	}
	str.Append(Temp);
	return str;
}
