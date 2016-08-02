<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="15008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="DecodeError.vi" Type="VI" URL="../DecodeError.vi"/>
		<Item Name="GetBeamDiameter.vi" Type="VI" URL="../GetBeamDiameter.vi"/>
		<Item Name="GetDarkOffset.vi" Type="VI" URL="../GetDarkOffset.vi"/>
		<Item Name="GetPower.vi" Type="VI" URL="../GetPower.vi"/>
		<Item Name="GetWavelength.vi" Type="VI" URL="../GetWavelength.vi"/>
		<Item Name="initialise.vi" Type="VI" URL="../initialise.vi"/>
		<Item Name="SetDarkOffset.vi" Type="VI" URL="../SetDarkOffset.vi"/>
		<Item Name="SetDarkOffsetCancel.vi" Type="VI" URL="../SetDarkOffsetCancel.vi"/>
		<Item Name="SetPowerRange.vi" Type="VI" URL="../SetPowerRange.vi"/>
		<Item Name="SetWavelength.vi" Type="VI" URL="../SetWavelength.vi"/>
		<Item Name="shutdown.vi" Type="VI" URL="../shutdown.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="PM100D Cancel Dark Adjustment.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Cancel Dark Adjustment.vi"/>
			<Item Name="PM100D Close.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Close.vi"/>
			<Item Name="PM100D Error Message.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Error Message.vi"/>
			<Item Name="PM100D Get Beam Diameter.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Get Beam Diameter.vi"/>
			<Item Name="PM100D Get Dark Offset.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Get Dark Offset.vi"/>
			<Item Name="PM100D Get Wavelength.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Get Wavelength.vi"/>
			<Item Name="PM100D Initialize.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Initialize.vi"/>
			<Item Name="PM100D Measure Power.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Measure Power.vi"/>
			<Item Name="PM100D Self-Test.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Self-Test.vi"/>
			<Item Name="PM100D Set Power Range.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Set Power Range.vi"/>
			<Item Name="PM100D Set Power Unit.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Set Power Unit.vi"/>
			<Item Name="PM100D Set Wavelength.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Set Wavelength.vi"/>
			<Item Name="PM100D Start Dark Offset Adjustment.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D Start Dark Offset Adjustment.vi"/>
			<Item Name="PM100D VXIpnp Error Converter.vi" Type="VI" URL="../../../../../../Program Files/IVI Foundation/VISA/Win64/PM100D/LabVIEW/PM100D.llb/PM100D VXIpnp Error Converter.vi"/>
			<Item Name="PM100D_64.dll" Type="Document" URL="PM100D_64.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="powerMeterUtil" Type="DLL">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{F67DC8D9-C1E1-49C5-BC0E-E87C3093901F}</Property>
				<Property Name="App_INI_GUID" Type="Str">{C24404D7-AF84-4708-858E-05A2156092BF}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{B3FB39D6-D6F2-4D00-A1F2-ED28A322ADAD}</Property>
				<Property Name="Bld_buildSpecDescription" Type="Str">Functions to control Thorlabs PM100D power meter (using LV drivers).
Jeff Lidgard, March 2016.</Property>
				<Property Name="Bld_buildSpecName" Type="Str">powerMeterUtil</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">..</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{73AB55F0-442F-486E-87D3-819D0B5B0A51}</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">powerMeterUtil.dll</Property>
				<Property Name="Destination[0].path" Type="Path">../powerMeterUtil.dll</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Dll_compatibilityWith2011" Type="Bool">false</Property>
				<Property Name="Dll_delayOSMsg" Type="Bool">true</Property>
				<Property Name="Dll_headerGUID" Type="Str">{9B35C2E4-BCA5-460C-8A9E-EE2E0B4D4158}</Property>
				<Property Name="Dll_includeTypeLibrary" Type="Bool">true</Property>
				<Property Name="Dll_libGUID" Type="Str">{96DBA7C9-667C-4C20-98B4-028482B9C7DB}</Property>
				<Property Name="Source[0].itemID" Type="Str">{C2E8CB00-D6E2-4F93-AA85-DA4556D1414A}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/GetBeamDiameter.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[10].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[10].itemID" Type="Ref">/My Computer/SetDarkOffsetCancel.vi</Property>
				<Property Name="Source[10].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[10].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[11].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[11].itemID" Type="Ref">/My Computer/DecodeError.vi</Property>
				<Property Name="Source[11].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[11].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/GetPower.vi</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[2].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/GetWavelength.vi</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[3].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/initialise.vi</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[4].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/SetPowerRange.vi</Property>
				<Property Name="Source[5].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[5].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[6].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[6].itemID" Type="Ref">/My Computer/SetWavelength.vi</Property>
				<Property Name="Source[6].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[6].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[7].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[7].itemID" Type="Ref">/My Computer/shutdown.vi</Property>
				<Property Name="Source[7].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[7].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[8].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[8].itemID" Type="Ref">/My Computer/GetDarkOffset.vi</Property>
				<Property Name="Source[8].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[8].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[9].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[9].itemID" Type="Ref">/My Computer/SetDarkOffset.vi</Property>
				<Property Name="Source[9].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[9].type" Type="Str">ExportedVI</Property>
				<Property Name="SourceCount" Type="Int">12</Property>
				<Property Name="TgtF_companyName" Type="Str">University of Oxford</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Functions to control Thorlabs PM100D power meter (using LV x64 drivers).
Jeff Lidgard, March 2016</Property>
				<Property Name="TgtF_internalName" Type="Str">powerMeterUtil</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Univserity of Oxford Copyright © 2016 </Property>
				<Property Name="TgtF_productName" Type="Str">powerMeterUtil</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{B492EE15-5BBF-4576-BC53-856C747203BD}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">powerMeterUtil.dll</Property>
			</Item>
		</Item>
	</Item>
</Project>
