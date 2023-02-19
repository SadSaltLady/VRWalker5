// Fill out your copyright notice in the Description page of Project Settings.


#include "DataTransmission.h"


// Sets default values for this component's properties
UDataTransmission::UDataTransmission()
{
	// Set this component to be initialized when the game starts, and to be ticked every frame.  You can turn these features
	// off to improve performance if you don't need them.
	PrimaryComponentTick.bCanEverTick = true;

	// ...
}


// Called when the game starts
void UDataTransmission::BeginPlay()
{
	Super::BeginPlay();

	// ...
	
}


// Called every frame
void UDataTransmission::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

	// ...
}

bool UDataTransmission::ConnectToServer(FString IP, int Port)
{
	ipAddress = IP;
	port = Port;
	
	FIPv4Address IPAdress; 
	FIPv4Address::Parse(ipAddress, IPAdress);
	
	//FIPv4Address EndPoint(); //EndPoint seems to be deprecated? 


	//TODO Figure out what all this is... Creates socket
	ListenSocket = FTcpSocketBuilder(TEXT("TCPSocket")).AsReusable();

	ISocketSubsystem* SocketSubsystem = ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM);
	ListenSocket->Bind(*SocketSubsystem->CreateInternetAddr());
	ListenSocket->Listen(8);


	
	//ListenSocket 

	return false;
}

bool UDataTransmission::TransmitToServer(FString data)
{
	return false;
}

void UDataTransmission::KillServerConnection()
{
}

