// Fill out your copyright notice in the Description page of Project Settings.

#include "SmoothConverters.h"
#include "Kismet/KismetMathLibrary.h"



FString USmoothConverters::VectorToNiceString(FVector input)
{
	FString comma = FString(TEXT(","));
	return FString::SanitizeFloat(input.X, 2) + comma + FString::SanitizeFloat(input.Y, 2) + comma + FString::SanitizeFloat(input.Z, 2);
}

FString USmoothConverters::VectorArrToString(TArray<FVector> vectors)
{
	FString FinalString = "";
	for (FVector& Each : vectors)
	{
		FinalString += VectorToNiceString(Each);
		FinalString += LINE_TERMINATOR;
	}
	return FinalString;
}

FRotator USmoothConverters::CalculateRotation(TArray<FVector> CaliPoints)
{
	FVector diff = CaliPoints[2] - CaliPoints[1];
	float angle = FMath::RadiansToDegrees(FMath::Atan2(diff.Y, diff.X)) + 180.f;
	return UKismetMathLibrary::RotatorFromAxisAndAngle(FVector(0.f, 0.f, 1.f), angle);
}

FVector USmoothConverters::CalculateOffset(TArray<FVector> CaliPoints, FVector C1, FVector C2, FVector C3)
{
	FVector delta = (CaliPoints[2] - C3) + (CaliPoints[1] - C2) + (CaliPoints[0] - C1);
	delta = (delta * FVector(1.f, 1.f, 0.f)) / 3.f;
	return delta;
}
