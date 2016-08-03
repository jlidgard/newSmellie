#include "extcode.h"
#ifdef __cplusplus
extern "C" {
#endif

/*!
 * AnalogIn_Create
 */
uint64_t __cdecl AnalogIn_Create(void);
/*!
 * AnalogIn_Destroy
 */
void __cdecl AnalogIn_Destroy(uint64_t AnalogIn);
/*!
 * AnalogIn_getVoltageIn
 */
double __cdecl AnalogIn_getVoltageIn(uint64_t AnalogIn);
/*!
 * AnalogOut_analogoutCountsToVolts
 */
double __cdecl AnalogOut_analogoutCountsToVolts(uint64_t AnalogOut, 
	int32_t counts);
/*!
 * AnalogOut_Create
 */
void __cdecl AnalogOut_Create(void);
/*!
 * AnalogOut_Destroy
 */
void __cdecl AnalogOut_Destroy(uint64_t AnalogOut);
/*!
 * AnalogOut_getDACIncrement
 */
int32_t __cdecl AnalogOut_getDACIncrement(uint64_t AnalogOut);
/*!
 * AnalogOut_getDACMaximum
 */
int32_t __cdecl AnalogOut_getDACMaximum(uint64_t AnalogOut);
/*!
 * AnalogOut_getDACMinimum
 */
int32_t __cdecl AnalogOut_getDACMinimum(uint64_t AnalogOut);
/*!
 * AnalogOut_getDACPins
 */
int32_t __cdecl AnalogOut_getDACPins(uint64_t AnalogOut);
/*!
 * AnalogOut_isDACPresent
 */
uint8_t __cdecl AnalogOut_isDACPresent(uint64_t AnalogOut);
/*!
 * AnalogOut_setDACCounts
 */
uint64_t __cdecl AnalogOut_setDACCounts(uint64_t AnalogOutIn, int32_t Counts, 
	int32_t Index);
/*!
 * BoardTemperature_Create
 */
uint64_t __cdecl BoardTemperature_Create(void);
/*!
 * BoardTemperature_Destroy
 */
void __cdecl BoardTemperature_Destroy(uint64_t BoardTemperature);
/*!
 * BoardTemperature_getBoardTemperatureCelsius
 */
double __cdecl BoardTemperature_getBoardTemperatureCelsius(
	uint32_t BoardTemperature);
/*!
 * ContinuousStrobe_continuousStrobeCountsToMicros
 */
double __cdecl ContinuousStrobe_continuousStrobeCountsToMicros(
	uint64_t ContinuousStrobe, int32_t counts);
/*!
 * ContinuousStrobe_Create
 */
uint64_t __cdecl ContinuousStrobe_Create(void);
/*!
 * ContinuousStrobe_Destroy
 */
void __cdecl ContinuousStrobe_Destroy(uint64_t ContinuousStrobe);
/*!
 * ContinuousStrobe_getContinuousStrobeDelayIncrement
 */
int32_t __cdecl ContinuousStrobe_getContinuousStrobeDelayIncrement(
	uint64_t ContinuousStrobe);
/*!
 * ContinuousStrobe_getContinuousStrobeDelayMaximum
 */
int32_t __cdecl ContinuousStrobe_getContinuousStrobeDelayMaximum(
	uint64_t ContinuousStrobe);
/*!
 * ContinuousStrobe_getContinuousStrobeDelayMinimum
 */
int32_t __cdecl ContinuousStrobe_getContinuousStrobeDelayMinimum(
	uint32_t ContinuousStrobe);
/*!
 * ContinuousStrobe_setContinuousStrobeDelay
 */
void __cdecl ContinuousStrobe_setContinuousStrobeDelay(
	uint64_t ContinuousStrobeIn, int32_t delay);
/*!
 * ExternalTriggerDelay_Create
 */
uint64_t __cdecl ExternalTriggerDelay_Create(void);
/*!
 * ExternalTriggerDelay_Destroy
 */
void __cdecl ExternalTriggerDelay_Destroy(void);
/*!
 * ExternalTriggerDelay_getExternalTriggerDelayIncrement
 */
int32_t __cdecl ExternalTriggerDelay_getExternalTriggerDelayIncrement(
	uint64_t ExternalTriggerDelay);
/*!
 * ExternalTriggerDelay_getExternalTriggerDelayMaximum
 */
int32_t __cdecl ExternalTriggerDelay_getExternalTriggerDelayMaximum(
	uint64_t ExternalTriggerDelay);
/*!
 * ExternalTriggerDelay_getExternalTriggerDelayMinimum
 */
int32_t __cdecl ExternalTriggerDelay_getExternalTriggerDelayMinimum(
	uint32_t ExternalTriggerDelay);
/*!
 * ExternalTriggerDelay_setExternalTriggerDelay
 */
void __cdecl ExternalTriggerDelay_setExternalTriggerDelay(
	uint64_t ExternalTriggerDelayIn, int32_t microseconds);
/*!
 * ExternalTriggerDelay_triggerDelayCountsToMicroseconds
 */
double __cdecl ExternalTriggerDelay_triggerDelayCountsToMicroseconds(
	uint64_t ExternalTriggerDelay, int32_t Counts);
/*!
 * SingleStrobe_Create
 */
uint64_t __cdecl SingleStrobe_Create(void);
/*!
 * SingleStrobe_Destroy
 */
void __cdecl SingleStrobe_Destroy(uint64_t SingleStrobe);
/*!
 * SingleStrobe_getSingleStrobeCountsToMicros
 */
double __cdecl SingleStrobe_getSingleStrobeCountsToMicros(
	uint64_t SingleStrobe, int32_t counts);
/*!
 * SingleStrobe_getSingleStrobeHigh
 */
int32_t __cdecl SingleStrobe_getSingleStrobeHigh(uint64_t SingleStrobe);
/*!
 * SingleStrobe_getSingleStrobeIncrement
 */
int32_t __cdecl SingleStrobe_getSingleStrobeIncrement(uint64_t SingleStrobe);
/*!
 * SingleStrobe_getSingleStrobeLow
 */
int32_t __cdecl SingleStrobe_getSingleStrobeLow(uint64_t SingleStrobe);
/*!
 * SingleStrobe_getSingleStrobeMaximum
 */
int32_t __cdecl SingleStrobe_getSingleStrobeMaximum(uint64_t SingleStrobe);
/*!
 * SingleStrobe_getSingleStrobeMinimum
 */
int32_t __cdecl SingleStrobe_getSingleStrobeMinimum(uint64_t SingleStrobe);
/*!
 * SingleStrobe_setSingleStrobeHigh
 */
void __cdecl SingleStrobe_setSingleStrobeHigh(uint64_t SingleStrobeIn, 
	int32_t SingleStrobeHigh);
/*!
 * SingleStrobe_setSingleStrobeLow
 */
void __cdecl SingleStrobe_setSingleStrobeLow(uint64_t SingleStrobeIn, 
	int32_t SingleStrobeLow);
/*!
 * Wrapper_closeAllSpectrometers
 */
void __cdecl Wrapper_closeAllSpectrometers(uint64_t WrapperIn);
/*!
 * Wrapper_Create
 */
uint64_t __cdecl Wrapper_Create(void);
/*!
 * Wrapper_Destroy
 */
void __cdecl Wrapper_Destroy(uint64_t Wrapper);
/*!
 * Wrapper_exportToGramsSPC
 */
void __cdecl Wrapper_exportToGramsSPC(uint64_t Wrapper, int32_t Index, 
	char OutputPathName[], double double_array[], char UserName[], 
	uint64_t *Wrapper2, uint8_t *returnType, int32_t len);
/*!
 * Wrapper_getApiVersion
 */
void __cdecl Wrapper_getApiVersion(uint64_t Wrapper, char APIVersion[], 
	int32_t len);
/*!
 * Wrapper_getBench
 */
uint64_t __cdecl Wrapper_getBench(uint64_t Wrapper, int32_t Index);
/*!
 * Wrapper_getBoxcarWidth
 */
int32_t __cdecl Wrapper_getBoxcarWidth(uint64_t Wrapper, int32_t Index);
/*!
 * Wrapper_getBuildNumber
 */
int32_t __cdecl Wrapper_getBuildNumber(uint64_t Wrapper);
/*!
 * Wrapper_getExternalTriggerMode
 */
int32_t __cdecl Wrapper_getExternalTriggerMode(uint64_t Wrapper, 
	int32_t Index);
/*!
 * Wrapper_getFeatureControllerAnalogIn
 */
uint64_t __cdecl Wrapper_getFeatureControllerAnalogIn(uint64_t Wrapper, 
	int32_t Index);
/*!
 * Wrapper_getFeatureControllerAnalogOut
 */
uint64_t __cdecl Wrapper_getFeatureControllerAnalogOut(uint64_t Wrapper, 
	int32_t Index);
/*!
 * Wrapper_getFeatureControllerBoardTemperature
 */
uint64_t __cdecl Wrapper_getFeatureControllerBoardTemperature(
	uint64_t Wrapper, int32_t index);
/*!
 * Wrapper_getFeatureControllerContinuousStrobe
 */
uint64_t __cdecl Wrapper_getFeatureControllerContinuousStrobe(
	uint64_t Wrapper, int32_t Index);
/*!
 * Wrapper_getFeatureControllerExternalTriggerDelay
 */
uint64_t __cdecl Wrapper_getFeatureControllerExternalTriggerDelay(
	uint64_t Wrapper, int32_t Index);
/*!
 * Wrapper_getFeatureControllerGPIO
 */
uint64_t __cdecl Wrapper_getFeatureControllerGPIO(uint64_t Wrapper, 
	int32_t Index);
/*!
 * Wrapper_getFeatureControllerIrradianceCalibrationFactor
 */
uint64_t __cdecl Wrapper_getFeatureControllerIrradianceCalibrationFactor(
	uint64_t Wrapper, int32_t index);
/*!
 * Wrapper_getFeatureControllerLS450
 */
uint64_t __cdecl Wrapper_getFeatureControllerLS450(uint64_t Wrapper, 
	int32_t SpectrometerIndex);
/*!
 * Wrapper_getFeatureControllerNonlinearityCorrectionProvider
 */
uint64_t __cdecl Wrapper_getFeatureControllerNonlinearityCorrectionProvider(
	uint64_t Wrapper, int32_t index);
/*!
 * Wrapper_getFeatureControllerSingleStrobe
 */
uint64_t __cdecl Wrapper_getFeatureControllerSingleStrobe(uint64_t Wrapper, 
	int32_t index);
/*!
 * Wrapper_getFeatureControllerSPIBus
 */
uint64_t __cdecl Wrapper_getFeatureControllerSPIBus(uint64_t Wrapper, 
	int32_t index);
/*!
 * Wrapper_getFeatureControllerStrayLightCorrection
 */
uint64_t __cdecl Wrapper_getFeatureControllerStrayLightCorrection(
	uint64_t Wrapper, int32_t index);
/*!
 * Wrapper_getFeatureControllerThermoElectric
 */
uint64_t __cdecl Wrapper_getFeatureControllerThermoElectric(uint64_t Wrapper, 
	int32_t Index);
/*!
 * Wrapper_getFeatureControllerVersion
 */
uint64_t __cdecl Wrapper_getFeatureControllerVersion(uint64_t Wrapper, 
	int32_t index);
/*!
 * Wrapper_getFeatureControllerWavelengthCalibraionProvider
 */
uint64_t __cdecl Wrapper_getFeatureControllerWavelengthCalibraionProvider(
	uint64_t Wrapper, int32_t index);
/*!
 * Wrapper_getFirmwareVersion
 */
void __cdecl Wrapper_getFirmwareVersion(uint64_t Wrapper, int32_t Index, 
	char Firmware[], int32_t len);
/*!
 * Wrapper_getIntegrationTime
 */
int32_t __cdecl Wrapper_getIntegrationTime(uint64_t Wrapper, int32_t Index);
/*!
 * Wrapper_getLastException
 */
void __cdecl Wrapper_getLastException(uint64_t Wrapper, char LastException[], 
	int32_t len);
/*!
 * Wrapper_getLastExceptionStackTrace
 */
void __cdecl Wrapper_getLastExceptionStackTrace(uint64_t Wrapper, 
	char LastExceptionStackTrace[], int32_t len);
/*!
 * Wrapper_getMaximumIntegrationTime
 */
int32_t __cdecl Wrapper_getMaximumIntegrationTime(uint64_t Wrapper, 
	int32_t Index);
/*!
 * Wrapper_getMaximumIntensity
 */
int32_t __cdecl Wrapper_getMaximumIntensity(uint64_t Wrapper, int32_t Index);
/*!
 * Wrapper_getMinimumIntegrationTime
 */
int32_t __cdecl Wrapper_getMinimumIntegrationTime(uint64_t Wrapper, 
	int32_t Index);
/*!
 * Wrapper_getName
 */
void __cdecl Wrapper_getName(int32_t Index, uint64_t Wrapper, 
	char SpectrometerName[], int32_t len);
/*!
 * Wrapper_getNumberOfDarkPixels
 */
int32_t __cdecl Wrapper_getNumberOfDarkPixels(uint64_t Wrapper, 
	int32_t Index);
/*!
 * Wrapper_getNumberOfPixels
 */
int32_t __cdecl Wrapper_getNumberOfPixels(uint64_t Wrapper, int32_t Index);
/*!
 * Wrapper_getNumberOfSpectrometersFound
 */
void __cdecl Wrapper_getNumberOfSpectrometersFound(uint64_t WrapperIn, 
	uint64_t *WrapperOut, int32_t *NumberOfSpectrometers);
/*!
 * Wrapper_getScansToAverage
 */
int32_t __cdecl Wrapper_getScansToAverage(uint64_t Wrapper, int32_t Index);
/*!
 * Wrapper_getSerialNumber
 */
void __cdecl Wrapper_getSerialNumber(uint64_t Wrapper, int32_t Index, 
	char SerialNumber[], int32_t len);
/*!
 * Wrapper_getSpectrum
 */
void __cdecl Wrapper_getSpectrum(uint64_t Wrapper, int32_t Index, 
	double SpectrumValues[], int32_t *Length, int32_t len);
/*!
 * Wrapper_getStrobeEnable
 */
int32_t __cdecl Wrapper_getStrobeEnable(uint64_t Wrapper, int32_t Index);
/*!
 * Wrapper_getWavelength
 */
double __cdecl Wrapper_getWavelength(uint64_t Wrapper, 
	int32_t SpectrometerIndex, int32_t Pixel);
/*!
 * Wrapper_getWavelengths
 */
void __cdecl Wrapper_getWavelengths(uint64_t Wrapper, int32_t Index, 
	double WLValues[], int32_t *Length, int32_t len);
/*!
 * Wrapper_highSpdAcq_AllocateBuffer
 */
void __cdecl Wrapper_highSpdAcq_AllocateBuffer(uint64_t WrapperIN, 
	uint32_t SpectrometerIndex, int32_t numberOfSpectra);
/*!
 * Wrapper_highSpdAcq_GetNumberOfSpectraAcquired
 */
int32_t __cdecl Wrapper_highSpdAcq_GetNumberOfSpectraAcquired(
	uint64_t Wrapper);
/*!
 * Wrapper_highSpdAcq_GetSpectrum
 */
void __cdecl Wrapper_highSpdAcq_GetSpectrum(uint64_t Wrapper, 
	int32_t SpectrumNumber, double SpectrumValues[], int32_t *Length, 
	int32_t len);
/*!
 * Wrapper_highSpdAcq_GetTimeStamp
 */
uint64_t __cdecl Wrapper_highSpdAcq_GetTimeStamp(uint64_t Wrapper, 
	int32_t SpectrumNumber);
/*!
 * Wrapper_highSpdAcq_StartAquisition
 */
void __cdecl Wrapper_highSpdAcq_StartAquisition(uint64_t WrapperIn, 
	int32_t SpectrometerIndex);
/*!
 * Wrapper_hightSpdAcq_IsSaturated
 */
uint8_t __cdecl Wrapper_hightSpdAcq_IsSaturated(uint64_t Wrapper, 
	int32_t SpectrumNumber);
/*!
 * Wrapper_hightSpdAcq_StopAcquisition
 */
void __cdecl Wrapper_hightSpdAcq_StopAcquisition(uint64_t WrapperIn);
/*!
 * Wrapper_insertKey
 */
uint8_t __cdecl Wrapper_insertKey(uint64_t Wrapper, char String[]);
/*!
 * Wrapper_isFeatureSupportedLS450
 */
uint8_t __cdecl Wrapper_isFeatureSupportedLS450(uint64_t Wrapper, 
	int32_t SpectrometerIndex);
/*!
 * Wrapper_isSaturated
 */
uint8_t __cdecl Wrapper_isSaturated(uint64_t Wrapper, int32_t Index);
/*!
 * Wrapper_openAllSpectrometers
 */
void __cdecl Wrapper_openAllSpectrometers(uint64_t WrapperIn, 
	int32_t *NumberOfSpectrometers);
/*!
 * Wrapper_openNetworkSpectrometer
 */
void __cdecl Wrapper_openNetworkSpectrometer(uint64_t Wrapper, 
	char IpAddress[], uint64_t *Wrapper2, int32_t *AssignedIndex);
/*!
 * Wrapper_removeKey
 */
void __cdecl Wrapper_removeKey(uint64_t WrapperIn);
/*!
 * Wrapper_setAutoToggleStrobeLampEnable
 */
void __cdecl Wrapper_setAutoToggleStrobeLampEnable(uint64_t WrapperIn, 
	int32_t Index, uint8_t Enable);
/*!
 * Wrapper_setBoxcarWidth
 */
void __cdecl Wrapper_setBoxcarWidth(uint64_t WrapperIn, int32_t Index, 
	int32_t BoxcarWidth);
/*!
 * Wrapper_setCorrectForDetectorNonlinearity
 */
void __cdecl Wrapper_setCorrectForDetectorNonlinearity(uint64_t WrapperIn, 
	int32_t Index, int32_t OnOff);
/*!
 * Wrapper_setCorrectForElectricalDark
 */
void __cdecl Wrapper_setCorrectForElectricalDark(uint64_t WrapperIn, 
	int32_t Index, int32_t OnOff);
/*!
 * Wrapper_setEEPromInfo
 */
void __cdecl Wrapper_setEEPromInfo(uint64_t WrapperIn, 
	int32_t SpectrometerIndex, int32_t Slot, char String[], uint64_t *WrapperOut, 
	uint8_t *Valid);
/*!
 * Wrapper_setExternalTriggerMode
 */
void __cdecl Wrapper_setExternalTriggerMode(uint64_t WrapperIn, 
	int32_t Index, int32_t TriggerMode);
/*!
 * Wrapper_setIntegrationTime
 */
void __cdecl Wrapper_setIntegrationTime(uint64_t WrapperIn, int32_t Index, 
	int32_t IntegrationTime);
/*!
 * Wrapper_setScansToAverage
 */
void __cdecl Wrapper_setScansToAverage(uint64_t WrapperIn, int32_t Index, 
	int32_t Average);
/*!
 * Wrapper_setStrobeEnable
 */
void __cdecl Wrapper_setStrobeEnable(uint64_t WrapperIn, int32_t Index, 
	int32_t OnOff);
/*!
 * Wrapper_stopAveraging
 */
void __cdecl Wrapper_stopAveraging(uint64_t WrapperIn, 
	int32_t SpectrometerIndex);

MgErr __cdecl LVDLLStatus(char *errStr, int errStrLen, void *module);

#ifdef __cplusplus
} // extern "C"
#endif

