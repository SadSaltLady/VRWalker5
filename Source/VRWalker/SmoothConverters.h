// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "SmoothConverters.generated.h"

/**
 * 
 */
UCLASS()
class VRWALKER_API USmoothConverters : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	
		UFUNCTION(BlueprintPure, Category = "File I/O")
		static FString VectorToNiceString(FVector input);

		UFUNCTION(BlueprintPure, Category = "File I/O")
		static FString VectorArrToString(TArray<FVector> vectors);

		UFUNCTION(BlueprintPure, Category = "Helper")
		static FRotator CalculateRotation(TArray<FVector> CaliPoints);

		UFUNCTION(BlueprintPure, Category = "Helper")
		static FVector CalculateOffset(TArray<FVector> CaliPoints, FVector C1, FVector C2, FVector C3);
};
