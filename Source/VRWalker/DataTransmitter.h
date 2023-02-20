// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "TcpSocketConnection.h"
#include "DataTransmitter.generated.h"

/** Please add a struct description */
USTRUCT(BlueprintType)
struct F_Data
{
	GENERATED_BODY()
public:
	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta = (DisplayName = "Time", MakeStructureDefaultValue = "0.000000"))
		double Time;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta = (DisplayName = "HeadPos", MakeStructureDefaultValue = "0.000000,0.000000,0.000000"))
		FVector HeadPos;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta = (DisplayName = "ControllerLeftPos", MakeStructureDefaultValue = "0.000000,0.000000,0.000000"))
		FVector ControllerLeftPos;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta = (DisplayName = "ControllerRightPos", MakeStructureDefaultValue = "0.000000,0.000000,0.000000"))
		FVector ControllerRightPos;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta = (DisplayName = "AngularAcceleration", MakeStructureDefaultValue = "0.000000,0.000000,0.000000"))
		FVector AngularAcceleration;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta = (DisplayName = "LinearAcceleration", MakeStructureDefaultValue = "0.000000,0.000000,0.000000"))
		FVector LinearAcceleration;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta = (DisplayName = "AngularVelocity", MakeStructureDefaultValue = "0.000000,0.000000,0.000000"))
		FVector AngularVelocity;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, meta = (DisplayName = "LinearVelocity", MakeStructureDefaultValue = "0.000000,0.000000,0.000000"))
		FVector LinearVelocity;
};

UCLASS()
class VRWALKER_API ADataTransmitter : public ATcpSocketConnection
{
	GENERATED_BODY()

public: 
	UPROPERTY(BlueprintReadWrite, EditAnywhere)
		FString IP = TEXT("127.0.0.1");
	UPROPERTY(BlueprintReadWrite, EditAnywhere)
		int Port = 54000;

public: 
	UFUNCTION(BlueprintCallable)
		FString ParseIntoCSV(TArray<F_Data> Data);


};
