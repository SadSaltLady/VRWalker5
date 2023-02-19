// MLKomar 2023

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "Runtime/Networking/Public/Networking.h"
#include "Runtime/Sockets/Public/Sockets.h"
#include "Runtime/Sockets/Public/SocketSubsystem.h"
#include "DataTransmission.generated.h"


UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class VRWALKER_API UDataTransmission : public UActorComponent
{
	GENERATED_BODY()

public:	
	// Sets default values for this component's properties
	UDataTransmission();
	

protected:
	// Called when the game starts
	virtual void BeginPlay() override;

	FSocket* ListenSocket;

public:	
	// Called every frame
	virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

	//Returns true if can connect to server... 
	UFUNCTION(BlueprintCallable, Category = "File Transmission")
		bool ConnectToServer(FString IP, int Port); 
	UFUNCTION(BlueprintCallable, Category = "File Transmission")
		bool TransmitToServer(FString data);
	UFUNCTION(BlueprintCallable, Category = "File Transmission")
		void KillServerConnection();
private: 


public: 
	UPROPERTY(VisibleAnywhere, BlueprintReadWrite)
		FString ipAddress = "127.0.0.1";
	UPROPERTY(VisibleAnywhere, BlueprintReadWrite)
		int port = 54000;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
		bool DidServerRespondYet = false;
	FString Response = TEXT("Nothing from sever yet!");
	FTimerHandle ServerResponseTimer;

		
};
