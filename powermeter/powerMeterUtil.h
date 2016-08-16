#include "extcode.h"
#ifdef __cplusplus
extern "C" {
#endif

/*!
 * Initialise
 */
int32_t __cdecl Initialise(char resourceName[], int16_t IDQueryDoQuery, 
	int16_t ResetDeviceResetDevice, uintptr_t *instrumentHandleOut);
/*!
 * This VI cancels a running dark current/zero offset adjustment procedure.
 * 
 */
int32_t __cdecl PM100DCancelDarkAdjustment(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut);
/*!
 * This VI closes the instrument driver session.
 * 
 * Note: The instrument must be reinitialized to use it again.
 */
int32_t __cdecl PM100DClose(uintptr_t *instrumentHandle);
/*!
 * This VI takes the error code returned by the instrument driver VIs 
 * interprets it and returns it as an user readable string. 
 * 
 * Status/error codes and description:
 * 
 * --- Instrument Driver Errors and Warnings ---
 * Status      Description
 * -------------------------------------------------
 *          0  No error (the call was successful).
 * 0x3FFF0085  Unknown Status Code     - VI_WARN_UNKNOWN_STATUS
 * 0x3FFC0901  WARNING: Value overflow - VI_INSTR_WARN_OVERFLOW (1073481985) 
 * 0x3FFC0902  WARNING: Value underrun - VI_INSTR_WARN_UNDERRUN (1073481986) 
 * 0x3FFC0903  WARNING: Value is NaN   - VI_INSTR_WARN_NAN (1073481987) 
 * 0xBFFC0001  Parameter 1 out of range. 
 * 0xBFFC0002  Parameter 2 out of range.
 * 0xBFFC0003  Parameter 3 out of range.
 * 0xBFFC0004  Parameter 4 out of range.
 * 0xBFFC0005  Parameter 5 out of range.
 * 0xBFFC0006  Parameter 6 out of range.
 * 0xBFFC0007  Parameter 7 out of range.
 * 0xBFFC0008  Parameter 8 out of range.
 * 0xBFFC0012  Error Interpreting instrument response.
 * 
 * --- Instrument Errors --- 
 * Range: 0xBFFC0700 .. 0xBFFC0CFF.
 * Calculation: Device error code + 0xBFFC0900.
 * Please see your device documentation for details.
 * 
 * --- VISA Errors ---
 * Please see your VISA documentation for details.
 * 
 */
int32_t __cdecl PM100DErrorMessage(uintptr_t *instrumentHandle, 
	int32_t ErrorCode0, uintptr_t *instrumentHandleOut, char ErrorMessage[], 
	int32_t len);
/*!
 * This VI selects the driver's error query mode.
 */
int32_t __cdecl PM100DErrorQueryMode(uintptr_t *instrumentHandle, 
	LVBoolean ModeAutomatic, uintptr_t *instrumentHandleOut);
/*!
 * This VI queries the instrument's error queue manually. 
 * Use this VI to query the instrument's error queue if the driver's error 
 * query mode is set to manual query. 
 * 
 * Notes:
 * (1) The returned values are stored in the drivers error store. You may use 
 * <Error Message> to get a descriptive text at a later point of time.
 */
int32_t __cdecl PM100DErrorQuery(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, int32_t *ErrorCode, char ErrorMessage[], 
	int32_t len);
/*!
 * This VI returns the input attenuation.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DGetAttenuation(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *Attenuation);
/*!
 * This VI returns the average count for measurement value generation.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DGetAverageCount(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, int16_t *AverageCount);
/*!
 * This VI is used to obtain the battery voltage readings from the instrument.
 * 
 * Remark:
 * (1) This VI is only supported with the PM160 and PM160T.
 * (2) This VI obtains the latest battery voltage measurement result.
 * (3) With the USB cable connected this VI will obtain the loading voltage. 
 * Only with USB cable disconnected (Bluetooth connection) the actual battery 
 * voltage can be read. 
 */
int32_t __cdecl PM100DGetBatteryVoltage(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *Voltage);
/*!
 * This VI returns the users beam diameter in millimeter [mm].
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * (2) Beam diameter set value is used for calculating power and energy 
 * density.
 * 
 */
int32_t __cdecl PM100DGetBeamDiameter(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *BeamDiameter);
/*!
 * This VI returns a human readable calibration message.
 * 
 */
int32_t __cdecl PM100DGetCalibrationMessage(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, char Message[], int32_t len);
/*!
 * This VI returns the current auto range mode.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, PM160, and PM200.
 * 
 */
int32_t __cdecl PM100DGetCurrentAutorangeMode(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, LVBoolean *CurrentAutorangeMode);
/*!
 * This VI returns the actual current range value.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, PM160, and PM200.
 * 
 */
int32_t __cdecl PM100DGetCurrentRange(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *CurrentValue);
/*!
 * This VI returns the current reference state.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, PM160, and PM200.
 * 
 */
int32_t __cdecl PM100DGetCurrentReferenceState(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, LVBoolean *CurrentReferenceState);
/*!
 * This VI returns the current reference value.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, PM160, and PM200.
 * 
 */
int32_t __cdecl PM100DGetCurrentReference(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *CurrentReferenceValue);
/*!
 * This VI returns the assumed sensor type for custom sensors without 
 * calibration data memory connected to the instrument.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DGetCustomSensorInputAdapterType(
	uintptr_t *instrumentHandle, uintptr_t *instrumentHandleOut, 
	int16_t *CustomSensorType);
/*!
 * This VI returns the state of a currently running dark current/zero offset 
 * adjustment procedure.
 * 
 */
int32_t __cdecl PM100DGetDarkAdjustmentState(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, int16_t *State);
/*!
 * This VI returns the dark/zero offset.
 * 
 * The VI is not supported with energy sensors.
 */
int32_t __cdecl PM100DGetDarkOffset(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *DarkOffset);
/*!
 * This VI returns the system date and time of the powermeter.
 * 
 * Notes:
 * (1) Date and time are displayed on instruments screen and are used as 
 * timestamp for data saved to memory card.
 * (2) The VI is only available on PM100D and PM200.
 */
int32_t __cdecl PM100DGetDateAndTime(uintptr_t *instrumentHandle, 
	int16_t *Second, int16_t *Minute, int16_t *Hour, int16_t *Day, 
	uintptr_t *instrumentHandleOut, int16_t *Year, int16_t *Month);
/*!
 * This VI returns the digital I/O port direction.
 * 
 * Note: The VI is available on PM200 only.
 */
int32_t __cdecl PM100DGetDigitalIODirection(uintptr_t *instrumentHandle, 
	LVBoolean *IO3, LVBoolean *IO2, uintptr_t *instrumentHandleOut, 
	LVBoolean *IO0, LVBoolean *IO1);
/*!
 * This VI returns the digital I/O output settings.
 * 
 * Note: The VI is available on PM200 only.
 */
int32_t __cdecl PM100DGetDigitalIOOutput(uintptr_t *instrumentHandle, 
	LVBoolean *IO3, LVBoolean *IO2, uintptr_t *instrumentHandleOut, 
	LVBoolean *IO0, LVBoolean *IO1);
/*!
 * This VI returns the actual digital I/O port level.
 * 
 * Note: The VI is available on PM200 only.
 */
int32_t __cdecl PM100DGetDigitalIOPort(uintptr_t *instrumentHandle, 
	LVBoolean *IO3, LVBoolean *IO2, uintptr_t *instrumentHandleOut, 
	LVBoolean *IO0, LVBoolean *IO1);
/*!
 * This VI returns the display brightness.
 * 
 */
int32_t __cdecl PM100DGetDisplayBrightness(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *Brightness);
/*!
 * This VI returns the display contrast of a PM100D.
 * 
 * Note: This VI is available on PM100D only
 */
int32_t __cdecl PM100DGetDisplayContrast(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *Contrast);
/*!
 * This VI returns the pyro sensor's energy range.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DGetEnergyRange(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *EnergyValue);
/*!
 * This VI returns the instrument's energy reference state.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DGetEnergyReferenceState(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, LVBoolean *EnergyReferenceState);
/*!
 * This VI returns the specified pyro sensor's energy reference value.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100USB, and PM200.
 * (2) The set value is used for calculating differences between the actual 
 * energy value and this energy reference value.
 * 
 */
int32_t __cdecl PM100DGetEnergyReference(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *EnergyReferenceValue);
/*!
 * This VI returns the instruments frequency range.
 * 
 * Remark:
 * The frequency of the input signal is calculated over at least 0.3s. So it 
 * takes at least 0.3s to get a new frequency value from the instrument.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, and PM100USB.
 * 
 */
int32_t __cdecl PM100DGetFrequencyRange(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *LowerFrequency, 
	double *UpperFrequency);
/*!
 * This VI returns the selected line frequency.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DGetLineFrequency(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, int16_t *LineFrequency);
/*!
 * This VI returns the peak detector threshold.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DGetPeakDetectorThreshold(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *PeakDetectorThreshold);
/*!
 * This VI returns the instrument's photodiode input filter state.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DGetPhotodiodeInputFilterState(
	uintptr_t *instrumentHandle, uintptr_t *instrumentHandleOut, 
	LVBoolean *PhotodiodeInputFilterState);
/*!
 * This VI returns the photodiode responsivity in ampere per watt [A/W].
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, PM160, and PM200.
 * 
 */
int32_t __cdecl PM100DGetPhotodiodeResponsivity(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *Responsivity);
/*!
 * This VI returns the power auto range mode.
 * 
 */
int32_t __cdecl PM100DGetPowerAutorangeMode(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, LVBoolean *PowerAutorangeMode);
/*!
 * This VI returns the actual power range value.
 * 
 */
int32_t __cdecl PM100DGetPowerRange(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *PowerValue);
/*!
 * This VI returns the power reference state.
 * 
 */
int32_t __cdecl PM100DGetPowerReferenceState(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, LVBoolean *PowerReferenceState);
/*!
 * This VI returns the power reference value.
 * 
 */
int32_t __cdecl PM100DGetPowerReference(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *PowerReferenceValue);
/*!
 * This VI returns the unit of the power value.
 * 
 */
int32_t __cdecl PM100DGetPowerUnit(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, int16_t *PowerUnit);
/*!
 * This VI returns the pyrosensor responsivity in volt per joule [V/J]
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DGetPyrosensorResponsivity(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *Responsivity);
/*!
 * This VI is used to obtain informations from the connected sensor like 
 * sensor name, serial number, calibration message, sensor type, sensor 
 * subtype and sensor flags.  
 * 
 * Remark:
 * The meanings of the obtained sensor type, subtype and flags are:
 * 
 * Sensor Types:
 *  SENSOR_TYPE_NONE (0)                0x00 // No sensor
 *  SENSOR_TYPE_PD_SINGLE (1)           0x01 // Photodiode sensor
 *  SENSOR_TYPE_THERMO (2)              0x02 // Thermopile sensor
 *  SENSOR_TYPE_PYRO (3)                0x03 // Pyroelectric sensor
 * 
 * Sensor Subtypes:
 *  SENSOR_SUBTYPE_NONE (0)             0x00 // No sensor
 *  
 * Sensor Subtypes Photodiode:
 *  SENSOR_SUBTYPE_PD_ADAPTER (1)       0x01 // Photodiode adapter
 *  SENSOR_SUBTYPE_PD_SINGLE_STD (2)    0x02 // Photodiode sensor
 *  SENSOR_SUBTYPE_PD_SINGLE_FSR (3)    0x03 // Photodiode sensor with 
 *                                         integrated filter
 *                                         identified by position 
 *  SENSOR_SUBTYPE_PD_SINGLE_STD_T (18)  0x12 // Photodiode sensor with
 *                                         temperature sensor
 * Sensor Subtypes Thermopile:
 *  SENSOR_SUBTYPE_THERMO_ADAPTER (1)   0x01 // Thermopile adapter
 *  SENSOR_SUBTYPE_THERMO_STD (2)       0x02 // Thermopile sensor
 *  SENSOR_SUBTYPE_THERMO_STD_T (18)     0x12 // Thermopile sensor with 
 *                                         temperature sensor
 * Sensor Subtypes Pyroelectric Sensor:
 *  SENSOR_SUBTYPE_PYRO_ADAPTER (1)     0x01 // Pyroelectric adapter
 *  SENSOR_SUBTYPE_PYRO_STD (2)         0x02 // Pyroelectric sensor
 *  SENSOR_SUBTYPE_PYRO_STD_T (18)       0x12 // Pyroelectric sensor with
 *                                         temperature sensor
 * Sensor Flags:
 *  PM100D_SENS_FLAG_IS_POWER (1)      0x0001 // Power sensor
 *  PM100D_SENS_FLAG_IS_ENERGY (2)     0x0002 // Energy sensor
 *  PM100D_SENS_FLAG_IS_RESP_SET (16)   0x0010 // Responsivity settable
 *  PM100D_SENS_FLAG_IS_WAVEL_SET (32)  0x0020 // Wavelength settable
 *  PM100D_SENS_FLAG_IS_TAU_SET (64)    0x0040 // Time constant settable
 *  PM100D_SENS_FLAG_HAS_TEMP (256)      0x0100 // With Temperature sensor 
 */
int32_t __cdecl PM100DGetSensorInformation(uintptr_t *instrumentHandle, 
	int16_t *SensorFlags, int16_t *SensorSubtype, int16_t *SensorType, 
	char SensorCalibrationMessage[], uintptr_t *instrumentHandleOut, 
	char SensorName[], char SensorSerialNumber[], int32_t len, int32_t len2, 
	int32_t len3);
/*!
 * This VI returns the thermopile acceleration mode.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DGetThermopileAcceleratorMode(
	uintptr_t *instrumentHandle, uintptr_t *instrumentHandleOut, 
	LVBoolean *ThermopileAcceleratorMode);
/*!
 * This VI returns the thermopile acceleration state.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DGetThermopileAcceleratorState(
	uintptr_t *instrumentHandle, uintptr_t *instrumentHandleOut, 
	LVBoolean *ThermopileAcceleratorState);
/*!
 * This VI returns the thermopile acceleration time constant in seconds [s].
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DGetThermopileAcceleratorTau(
	uintptr_t *instrumentHandle, int16_t AttributeSetValue, 
	uintptr_t *instrumentHandleOut, double *ThermopileAcceleratorTau);
/*!
 * This VI returns the thermopile responsivity in volt per watt [V/W]
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DGetThermopileResponsivity(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *Responsivity);
/*!
 * This VI returns the voltage auto range mode.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DGetVoltageAutorangeMode(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, LVBoolean *VoltageAutorangeMode);
/*!
 * This VI returns the actual voltage range value.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DGetVoltageRange(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *VoltageValue);
/*!
 * This VI returns the voltage reference state.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DGetVoltageReferenceState(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, LVBoolean *VoltageReferenceState);
/*!
 * This VI returns the voltage reference value.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DGetVoltageReference(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *VoltageReferenceValue);
/*!
 * This VI returns the users wavelength in nanometer [nm].
 * 
 * Remark:
 * Wavelength set value is used for calculating power.
 * 
 */
int32_t __cdecl PM100DGetWavelength(uintptr_t *instrumentHandle, 
	int16_t AttributeSetValue, uintptr_t *instrumentHandleOut, 
	double *Wavelength);
/*!
 * This VI returns the device identification information.
 */
int32_t __cdecl PM100DIdentificationQuery(uintptr_t *instrumentHandle, 
	char FirmwareRevision[], char SerialNumber[], uintptr_t *instrumentHandleOut, 
	char ManufacturerName[], char DeviceName[], int32_t len, int32_t len2, 
	int32_t len3, int32_t len4);
/*!
 * This VI initializes the instrument driver session and performs the 
 * following initialization actions:
 * 
 * (1) Opens a session to the Default Resource Manager resource and a session 
 * to the specified device using the Resource Name  specified.
 * (2) Performs an identification query on the instrument.
 * (3) Resets the instrument to a known state.
 * (4) Sends initialization commands to the instrument.
 * (5) Returns an instrument handle which is used to distinguish between 
 * different sessions of this instrument driver.
 * 
 * Notes:
 * (1) Each time this VI is invoked a unique session is opened.  
 */
int32_t __cdecl PM100DInitialize(uintptr_t *resourceName, 
	LVBoolean IDQueryDoQuery, LVBoolean ResetDeviceResetDevice, 
	uintptr_t *instrumentHandleOut);
/*!
 * This VI is used to obtain voltage readings from the instrument's auxiliary 
 * AD0 input. 
 * 
 * Note: The VI is available on PM200 only.
 */
int32_t __cdecl PM100DMeasureAuxiliaryAD0Voltage(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *Voltage);
/*!
 * This VI is used to obtain voltage readings from the instrument's auxiliary 
 * AD1 input. 
 * 
 * Note: The VI is available on PM200 only.
 */
int32_t __cdecl PM100DMeasureAuxiliaryAD1Voltage(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *Voltage);
/*!
 * This VI is used to obtain current readings from the instrument. 
 * 
 * Remark:
 * This VI starts a new measurement cycle and after finishing measurement the 
 * result is received. Subject to the actual Average Count this may take up to 
 * seconds. Refer to <Set/Get Average Count>. 
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160, and PM200.
 * 
 */
int32_t __cdecl PM100DMeasureCurrent(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *Current);
/*!
 * This VI is used to obtain energy density readings from the instrument. 
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DMeasureEnergyDensity(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *EnergyDensity);
/*!
 * This VI is used to obtain energy readings from the instrument. 
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DMeasureEnergy(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *Energy);
/*!
 * This VI is used to obtain relative humidity readings from the Environment 
 * Monitor Module (EMM) connected to the instrument. 
 * 
 * Note: The VI is available on PM200 only. The VI will return an error when 
 * no EMM is connected.
 */
int32_t __cdecl PM100DMeasureEnvironmentalHumidity(
	uintptr_t *instrumentHandle, uintptr_t *instrumentHandleOut, 
	double *Humidity);
/*!
 * This VI is used to obtain temperature readings from the Environment Monitor 
 * Module (EMM) connected to the instrument. 
 * 
 * Note: The VI is available on PM200 only. The VI will return an error when 
 * no EMM is connected.
 */
int32_t __cdecl PM100DMeasureEnvironmentalTemperature(
	uintptr_t *instrumentHandle, uintptr_t *instrumentHandleOut, 
	double *Temperature);
/*!
 * This VI is used to obtain frequency readings from the instrument. 
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DMeasureFrequency(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *Frequency);
/*!
 * This VI is used to obtain power density readings from the instrument. 
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DMeasurePowerDensity(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *PowerDensity);
/*!
 * This VI is used to obtain power readings from the instrument. 
 * 
 * Remark:
 * This VI starts a new measurement cycle and after finishing measurement the 
 * result is received. Subject to the actual Average Count this may take up to 
 * seconds. Refer to <Set/Get Average Count>. 
 */
int32_t __cdecl PM100DMeasurePower(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *Power);
/*!
 * This VI is used to obtain voltage readings from the instrument. 
 * 
 * Remark:
 * This VI starts a new measurement cycle and after finishing measurement the 
 * result is received. Subject to the actual Average Count this may take up to 
 * seconds. Refer to <Set/Get Average Count>. 
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DMeasureVoltage(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, double *Voltage);
/*!
 * This VI reads directly from the instrument.
 * 
 */
int32_t __cdecl PM100DReadFromInstrument(uintptr_t *instrumentHandle, 
	uint32_t Size, uintptr_t *instrumentHandleOut, char Buffer[], 
	uint32_t *ReturnCount0, int32_t len);
/*!
 * This VI reads the content of any readable instrument register. Refer to 
 * your instrument's user's manual for more details on status structure 
 * registers.
 * 
 */
int32_t __cdecl PM100DReadRegister(uintptr_t *instrumentHandle, 
	int16_t RegisterIDStatusByteRegister, uintptr_t *instrumentHandleOut, 
	int16_t *Value);
/*!
 * This VI resets the device.
 */
int32_t __cdecl PM100DReset(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut);
/*!
 * This VI returns the revision numbers of the instrument driver and the 
 * device firmware.
 */
int32_t __cdecl PM100DRevisionQuery(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, char InstrumentDriverRevision[], 
	char FirmwareRevision[], int32_t len, int32_t len2);
/*!
 * This VI runs the device self test routine and returns the test result.
 */
int32_t __cdecl PM100DSelfTest(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut, int16_t *SelfTestResult, 
	char SelfTestMessage[], int32_t len);
/*!
 * This VI sets the input attenuation.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetAttenuation(uintptr_t *instrumentHandle, 
	double Attenuation00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the average count for measurement value generation.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetAverageCount(uintptr_t *instrumentHandle, 
	int16_t AverageCount1, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the users beam diameter in millimeter [mm].
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * (2) Beam diameter set value is used for calculating power and energy 
 * density.
 * 
 */
int32_t __cdecl PM100DSetBeamDiameter(uintptr_t *instrumentHandle, 
	double BeamDiameter00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the current auto range mode.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, PM160, and PM200.
 * 
 */
int32_t __cdecl PM100DSetCurrentAutorangeMode(uintptr_t *instrumentHandle, 
	uint16_t CurrentAutorangeModeON, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the sensor's current range.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, PM160, and PM200.
 * 
 */
int32_t __cdecl PM100DSetCurrentRange(uintptr_t *instrumentHandle, 
	double CurrentToMeasure00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the current reference state.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, PM160, and PM200.
 * 
 */
int32_t __cdecl PM100DSetCurrentReferenceState(uintptr_t *instrumentHandle, 
	uint16_t CurrentReferenceStateOFF, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the current reference value.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, PM160, and PM200.
 * 
 */
int32_t __cdecl PM100DSetCurrentReference(uintptr_t *instrumentHandle, 
	double CurrentReferenceValue00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the sensor type to assume for custom sensors without 
 * calibration data memory connected to the instrument.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetCustomSensorInputAdapterType(
	uintptr_t *instrumentHandle, int16_t CustomSensorTypePhotodiode, 
	uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the system date and time of the powermeter.
 * 
 * Notes:
 * (1) Date and time are displayed on instruments screen and are used as 
 * timestamp for data saved to memory card.
 * (2) The VI is only available on PM100D and PM200.
 */
int32_t __cdecl PM100DSetDateAndTime(uintptr_t *instrumentHandle, 
	int16_t Year2009, int16_t Month1, int16_t Day1, int16_t Hour14, 
	int16_t Minute0, int16_t Second0, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the digital I/O port direction.
 * 
 * Note: The VI is available on PM200 only.
 */
int32_t __cdecl PM100DSetDigitalIODirection(uintptr_t *instrumentHandle, 
	LVBoolean IO0Input, LVBoolean IO1Input, LVBoolean IO2Input, 
	LVBoolean IO3Input, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the digital I/O outputs.
 * 
 * Note: Only ports configured as outputs are affected by this VI. Use <Set 
 * Digital I/O Direction> to configure ports as outputs.
 * 
 * Note: The VI is available on PM200 only.
 */
int32_t __cdecl PM100DSetDigitalIOOutput(uintptr_t *instrumentHandle, 
	LVBoolean IO0High, LVBoolean IO1High, LVBoolean IO2High, LVBoolean IO3High, 
	uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the display brightness.
 */
int32_t __cdecl PM100DSetDisplayBrightness(uintptr_t *instrumentHandle, 
	double Brightness10, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the display contrast of a PM100D.
 * 
 * Note: The VI is available on PM100D only.
 */
int32_t __cdecl PM100DSetDisplayContrast(uintptr_t *instrumentHandle, 
	double Contrast05, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the pyro sensor's energy range.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetEnergyRange(uintptr_t *instrumentHandle, 
	double EnergyToMeasure00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the instrument's energy reference state.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetEnergyReferenceState(uintptr_t *instrumentHandle, 
	uint16_t EnergyReferenceStateOFF, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the pyro sensor's energy reference value
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100USB, and PM200.
 * (2) This value is used for calculating differences between the actual 
 * energy value and this energy reference value.
 * 
 */
int32_t __cdecl PM100DSetEnergyReference(uintptr_t *instrumentHandle, 
	double EnergyReferenceValue00, uintptr_t *instrumentHandleOut);
/*!
 * This VI selects the line frequency.
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetLineFrequency(uintptr_t *instrumentHandle, 
	double LineFrequency50Hz, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the peak detector threshold.
 * 
 * Remark:
 * Peak detector threshold is in percent [%] of the maximum from the actual 
 * measurements range.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetPeakDetectorThreshold(uintptr_t *instrumentHandle, 
	double PeakDetectorThreshold00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the instrument's photodiode input filter state.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetPhotodiodeInputFilterState(
	uintptr_t *instrumentHandle, uint16_t PhotodiodeInputFilterStateON, 
	uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the photodiode responsivity in ampere per watt [A/W].
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetPhotodiodeResponsivity(uintptr_t *instrumentHandle, 
	double Response00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the power auto range mode.
 * 
 */
int32_t __cdecl PM100DSetPowerAutorangeMode(uintptr_t *instrumentHandle, 
	uint16_t PowerAutorangeModeON, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the sensor's power range.
 * 
 */
int32_t __cdecl PM100DSetPowerRange(uintptr_t *instrumentHandle, 
	double PowerToMeasure00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the power reference state.
 * 
 */
int32_t __cdecl PM100DSetPowerReferenceState(uintptr_t *instrumentHandle, 
	uint16_t PowerReferenceStateOFF, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the power reference value.
 * 
 */
int32_t __cdecl PM100DSetPowerReference(uintptr_t *instrumentHandle, 
	double PowerReferenceValue00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the unit of the power value.
 * 
 */
int32_t __cdecl PM100DSetPowerUnit(uintptr_t *instrumentHandle, 
	int16_t PowerUnitWatt, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the pyrosensor responsivity in volt per joule [V/J]
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetPyrosensorResponsivity(uintptr_t *instrumentHandle, 
	double Response00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the thermopile acceleration auto mode.
 * 
 * While thermopile acceleration improves displaying changing measurement 
 * values it unfortunately adds extra noise which can become noticeable on 
 * constant values measurements. With acceleration mode set to AUTO the 
 * instrument enables the acceleration circuitry after big measurement values 
 * for five times of "Tau". See also VIs "Set Thermopile Accelerator Tau" and 
 * "Set Thermopile Accelerator  State".
 * 
 * With calling "Set Thermopile Accelerator State" the accelerator mode will 
 * always be reset to MANUAL.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DSetThermopileAcceleratorMode(
	uintptr_t *instrumentHandle, uint16_t ThermopileAcceleratorModeON, 
	uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the thermopile acceleration state.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DSetThermopileAcceleratorState(
	uintptr_t *instrumentHandle, uint16_t ThermopileAcceleratorStateON, 
	uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the thermopile acceleration time constant in seconds [s].
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetThermopileAcceleratorTau(
	uintptr_t *instrumentHandle, double ThermopileAcceleratorTau00, 
	uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the thermopile responsivity in volt per watt [V/W]
 * 
 * Notes:
 * (1) The VI is only available on PM100A, PM100D, PM100USB, and PM200.
 * 
 */
int32_t __cdecl PM100DSetThermopileResponsivity(uintptr_t *instrumentHandle, 
	double Response00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the voltage auto range mode.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DSetVoltageAutorangeMode(uintptr_t *instrumentHandle, 
	uint16_t VoltageAutorangeModeON, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the sensor's voltage range.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DSetVoltageRange(uintptr_t *instrumentHandle, 
	double VoltageToMeasure00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the voltage reference state.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DSetVoltageReferenceState(uintptr_t *instrumentHandle, 
	uint16_t VoltageReferenceStateOFF, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the voltage reference value.
 * 
 * Notes:
 * (1) The VI is only available on PM100D, PM100A, PM100USB, PM160T, and 
 * PM200.
 * 
 */
int32_t __cdecl PM100DSetVoltageReference(uintptr_t *instrumentHandle, 
	double VoltageReferenceValue00, uintptr_t *instrumentHandleOut);
/*!
 * This VI sets the users wavelength in nanometer [nm].
 * 
 * Remark:
 * Wavelength set value is used for calculating power.
 * 
 */
int32_t __cdecl PM100DSetWavelength(uintptr_t *instrumentHandle, 
	double Wavelength00, uintptr_t *instrumentHandleOut);
/*!
 * This VI starts the dark current/zero offset adjustment procedure.
 * 
 * Remark: 
 * (1) You have to darken the input before starting dark/zero adjustment.
 * (2) You can get the state of dark/zero adjustment with <Get Dark Adjustment 
 * State>
 * (3) You can stop dark/zero adjustment with <Cancel Dark Adjustment>
 * (4) You get the dark/zero value with <Get Dark Offset>
 * (5) Energy sensors do not support this VI
 */
int32_t __cdecl PM100DStartDarkOffsetAdjustment(uintptr_t *instrumentHandle, 
	uintptr_t *instrumentHandleOut);
/*!
 * This VI converts error codes from VXIPnp instrument driver to standard 
 * LabVIEW error codes.  If an error is detected the VI builds the appropriate 
 * error cluster that is readable by one of the error handlers supplied with 
 * LabVIEW.
 */
int32_t __cdecl PM100DVXIpnpErrorConverter(uint32_t instrumentHandle, 
	int32_t CVIErrorCode0, char NameOfVI[], uint32_t *instrumentHandleOut);
/*!
 * This VI writes the content of any writable instrument register. Refer to 
 * your instrument's user's manual for more details on status structure 
 * registers.
 * 
 */
int32_t __cdecl PM100DWriteRegister(uintptr_t *instrumentHandle, 
	int16_t RegisterIDServiceRequestEnable, int16_t Value0, 
	uintptr_t *instrumentHandleOut);
/*!
 * This VI writes directly to the instrument.
 */
int32_t __cdecl PM100DWriteToInstrument(uintptr_t *instrumentHandle, 
	char CommandRSTN[], uintptr_t *instrumentHandleOut);
/*!
 * GetTaskHandle
 */
int32_t __cdecl GetTaskHandle(char resourceName[], 
	uintptr_t *instrumentHandleOut);

MgErr __cdecl LVDLLStatus(char *errStr, int errStrLen, void *module);

#ifdef __cplusplus
} // extern "C"
#endif

