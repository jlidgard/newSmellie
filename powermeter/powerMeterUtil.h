#include "extcode.h"
#ifdef __cplusplus
extern "C" {
#endif

/*!
 * GetBeamDiameter
 */
int32_t __cdecl GetBeamDiameter(char resourceName[], 
	double *BeamDiameterSqMm);
/*!
 * GetPower
 */
int32_t __cdecl GetPower(char resourceName[], double *Power);
/*!
 * GetWavelength
 */
int32_t __cdecl GetWavelength(char resourceName[], double *Wavelength);
/*!
 * Initialise
 */
int32_t __cdecl Initialise(char resourceName[], int16_t *SelfTestResult, 
	char SelfTestMessage[], int32_t len);
/*!
 * SetPowerRange
 */
int32_t __cdecl SetPowerRange(char resourceName[], double PowerToMeasure00);
/*!
 * SetWavelength
 */
int32_t __cdecl SetWavelength(char resourceName[], double WavelengthNm);
/*!
 * Shutdown
 */
int32_t __cdecl Shutdown(char resourceName[]);
/*!
 * GetDarkOffset
 */
int32_t __cdecl GetDarkOffset(char resourceName[], double *DarkOffset);
/*!
 * SetDarkOffset
 */
int32_t __cdecl SetDarkOffset(char resourceName[]);
/*!
 * SetDarkOffsetCancel
 */
int32_t __cdecl SetDarkOffsetCancel(char resourceName[]);
/*!
 * DecodeError
 */
int32_t __cdecl DecodeError(char resourceName[], int32_t ErrorCode0, 
	char ErrorMessage[], int32_t len);

MgErr __cdecl LVDLLStatus(char *errStr, int errStrLen, void *module);

#ifdef __cplusplus
} // extern "C"
#endif

