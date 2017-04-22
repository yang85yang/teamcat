#alt + shift + e    runs the code

import math;

#These are the values that should be sent to this file
def CalculateWheelVelocity(targetX, targetY):

    #Declare some of the needed variables
    RobotHomeX = 0.0;
    RobotHomeY = 0.0;
    wheelOffset = 1.0; # distance from wheel to wheel drive center
    wheelLHomeX = 0.0;
    wheelRHomeX = 0.0;
    wheelLHomeY = 0.0;
    wheelRHomeY = 0.0;
    wheelRTargetX = 0.0;
    wheelLTargetX = 0.0;
    wheelRTargetY = 0.0;
    wheelLTargetY = 0.0;
    wheel_opp = 0.0;
    wheel_adj = 0.0;
    driveDistance = 0.0;
    thetaCarInv = 0.0;
    thetaCar = 0.0;  #Angle of the point in reference to the origin
    thetaRef = 0.0;
    wheelLVelocity = 0.0;
    wheelRVelocity = 0.0;

    driveDistance = math.sqrt((targetX * targetX) + (targetY * targetY));
    thetaCarInv = targetX / driveDistance;
    thetaCar = math.acos(thetaCarInv);#Angle of the point in reference to the origin

    if targetX > 0:
        thetaCar = thetaCar - 90;
        thetaRef = 90 - abs(thetaCar);
    if targetX < 0:
        thetaCar = thetaCar - 90;
        thetaRef = 90 - thetaCar;
    if targetX == 0:
        thetaCar = 0;

    # Set wheel home positions:
    wheelLHomeX = RobotHomeX - wheelOffset;
    wheelRHomeX = RobotHomeX + wheelOffset;
    wheelLHomeY = RobotHomeY;
    wheelRHomeY = RobotHomeY;

    # Calculate Targe wheel positions:
    #SOH
    wheel_opp = math.sin(thetaRef) * wheelOffset;
    wheelLTargetX = targetX - wheel_opp;
    wheelRTargetX = targetX + wheel_opp;
    wheel_adj = math.sqrt(wheelOffset - (wheel_opp * wheel_opp));

    if thetaCar < 0:
        wheelLTargetY = targetY + wheel_adj;
        wheelRTargetY = targetY - wheel_adj;
    if thetaCar > 0:
        wheelLTargetY = targetY - wheel_adj;
        wheelRTargetY = targetY + wheel_adj;

    # declare more needed variables
    changeInXL = 0.0;
    changeInYL = 0.0;
    changeInXR = 0.0;
    changeInYR = 0.0;
    wheelLTravel = 0.0;
    wheelRTravel = 0.0;

    changeInXL = wheelLTargetX - wheelLHomeX;
    changeInYL = wheelLTargetY - wheelLHomeY;
    changeInXR = wheelRTargetX - wheelRHomeX;
    changeInYR = wheelRTargetY - wheelRHomeY;
    wheelLTravel = math.sqrt((changeInXL * changeInXL) + (changeInYL * changeInYL));
    wheelRTravel = math.sqrt((changeInXR * changeInXR) + (changeInYR * changeInYR));

    # Set wheel velocity ratio
    if wheelLTravel > wheelRTravel:
        wheelRVelocity = 1;
        wheelLVelocity = wheelLTravel / wheelRTravel;
    if wheelLTravel < wheelRTravel:
        wheelLVelocity = 1;
        wheelRVelocity = wheelRTravel / wheelLTravel;
    if wheelLTravel == wheelRTravel:
        wheelLVelocity = 1;
        wheelRVelocity = 1;

    print("Left Wheel Velocity: ",wheelLVelocity);
    print("Right Wheel Velocity ",wheelRVelocity);

if __name__ == '__main__':
    CalculateWheelVelocity(4, 5)