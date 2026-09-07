#
# PySNMP MIB module CISCO-VOA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOA-MIB
# Source digest sha256:1c7d8fa961926b067716c7905a4e4fed4e62b86615fa81e562d1afdb419b94f1
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
OpticalIfDirection, = mibBuilder.importSymbols("CISCO-OPTICAL-MONITOR-MIB", "OpticalIfDirection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp")
ciscoVoaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 262))
ciscoVoaMIB.setRevisions(('2002-05-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoaMIB.setRevisionsDescriptions(('The initial revision of this MIB.',))
if mibBuilder.loadTexts: ciscoVoaMIB.setLastUpdated('2002-05-07 00:00')
if mibBuilder.loadTexts: ciscoVoaMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoaMIB.setContactInfo('Cisco Systems\n                    Customer Service\n\n                    Postal: 170 W Tasman Drive\n                    San Jose, CA 95134\n\n                    Tel: +1 800 553-NETS\n\n                    E-mail: cs-dwdm@cisco.com')
if mibBuilder.loadTexts: ciscoVoaMIB.setDescription('This MIB module defines objects to configure and manage the\n        Variable Optical Attenuator (VOA) modules.\n\n        VOA modules are typically used to attenuate channels added\n        by a network element, in order to equalize the input power of\n        each wavelength before the multiplexed signal consisting of\n        all wavelengths is sent through an EDFA.  There may be\n        a separate VOA per channel, one VOA per band of wavelengths,\n        or one VOA for the pass through wavelengths.\n\n        VOA modules are also often used before terminating optical\n        wavelengths at optical receivers, in order to avoid receiver\n        saturation.\n\n        The VOAs may be present on various modules within the network\n        element, for example, on an Optical Add/Drop Multiplexer\n        (OADM) module, on the same module as an optical transceiver,\n        or on a separate module of its own.\n        ')
class OpticalPowerInDbm(TextualConvention, Integer32):
    description = "An integer value that gives the optical power level in 1/10ths\n        of dBm.\n        Example: The value -300 represents a power level of -30.0 dBm.\n\n        The distinguished value of '-1000' indicates that the object\n        has not yet been initialized.\n        "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-400, 250), ValueRangeConstraint(-1000, -1000), )
class OpticalAttenInDb(TextualConvention, Integer32):
    description = 'An integer value that gives the attenuation level in\n        1/10ths of dB. \n        Example: The value 80 represents an attenuation\n        level of 8.0 dB.\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 400)

cVoaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 1))
cVoaBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1))
cVoaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cVoaTable.setStatus('current')
if mibBuilder.loadTexts: cVoaTable.setDescription('This table provides objects to configure and control the \n        attenuation on VOAs.')
cVoaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-VOA-MIB", "cVoaDirection"))
if mibBuilder.loadTexts: cVoaEntry.setStatus('current')
if mibBuilder.loadTexts: cVoaEntry.setDescription('An entry in the cVoaTable provides objects to configure and\n        control the attenuation level of a VOA at an interface, for\n        a given direction.')
cVoaDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 1), OpticalIfDirection()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cVoaDirection.setStatus('current')
if mibBuilder.loadTexts: cVoaDirection.setDescription('This is the second index into the cVoaTable and indicates\n        the direction for which the attenuation level at this\n        interface is being controlled, in this entry.')
cVoaAttenuationControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("automatic", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaAttenuationControlMode.setStatus('current')
if mibBuilder.loadTexts: cVoaAttenuationControlMode.setDescription("This object is used to set the mode of controlling the\n        attenuation level of a VOA at an interface.\n\n        When the mode is set to 'manual', the attenuation level is\n        configured manually, by setting the desired attenuation\n        level in the cVoaAttenuation object. The cVoaDesiredPower\n        object does not apply in this case.\n\n        When the mode is set to 'automatic', the attenuation level\n        is continuously adjusted to maintain a desired power level,\n        after attenuation. The desired optical power level after\n        attenuation is configured using the cVoaDesiredPower object.\n        The cVoaAttenuation object cannot be configured in this case,\n        but it indicates the attenuation level derived from the\n        desired power level.\n\n        The automatic mode of controlling attenuation should not be\n        used when the monitored power level includes multiple\n        wavelengths, since the power level monitor cannot distinguish\n        between a decrease in power across all wavelengths, versus a\n        loss of power of some but not all wavelengths. If some but not\n        all wavelengths go down, this would cause the attenuation level\n        to be automatically decreased, leading to an increase in the\n        power level of the remaining wavelengths.")
cVoaAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 3), OpticalAttenInDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaAttenuation.setStatus('current')
if mibBuilder.loadTexts: cVoaAttenuation.setDescription("This object indicates the attenuation level applied at the\n        interface.\n\n        When the cVoaAttenuationControlMode object is set to 'manual', \n        the attenuation level may be specified by setting this object.")
cVoaAttenuationLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVoaAttenuationLastChange.setStatus('current')
if mibBuilder.loadTexts: cVoaAttenuationLastChange.setDescription('This object indicates the value of sysUpTime at the last\n        time the attenuation level was adjusted at this interface,\n        in the given direction.')
cVoaDesiredPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 5), OpticalPowerInDbm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaDesiredPower.setStatus('current')
if mibBuilder.loadTexts: cVoaDesiredPower.setDescription("This object indicates the desired optical power level,\n        after attenuation, at the interface. \n\n        This object applies only when the cVoaAttenuationControlMode\n        object is set to 'automatic'. In this mode, the attenuation\n        level is continuously adjusted to maintain the desired \n        power level, after attenuation, as specified by this object.")
cVoaMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3))
cVoaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 1))
cVoaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 2))
cVoaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 1, 1)).setObjects(("CISCO-VOA-MIB", "cVoaMIBBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoaMIBCompliance = cVoaMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cVoaMIBCompliance.setDescription('The compliance statement for platforms that provide\n        configuration and control of VOA modules.')
cVoaMIBBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 2, 1)).setObjects(("CISCO-VOA-MIB", "cVoaAttenuationControlMode"), ("CISCO-VOA-MIB", "cVoaAttenuation"), ("CISCO-VOA-MIB", "cVoaAttenuationLastChange"), ("CISCO-VOA-MIB", "cVoaDesiredPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoaMIBBaseGroup = cVoaMIBBaseGroup.setStatus('current')
if mibBuilder.loadTexts: cVoaMIBBaseGroup.setDescription('A collection of mandatory managed objects that provide basic\n        configuration and control of the VOA modules.')
mibBuilder.exportSymbols("CISCO-VOA-MIB", OpticalAttenInDb=OpticalAttenInDb, OpticalPowerInDbm=OpticalPowerInDbm, PYSNMP_MODULE_ID=ciscoVoaMIB, cVoaAttenuation=cVoaAttenuation, cVoaAttenuationControlMode=cVoaAttenuationControlMode, cVoaAttenuationLastChange=cVoaAttenuationLastChange, cVoaBaseGroup=cVoaBaseGroup, cVoaDesiredPower=cVoaDesiredPower, cVoaDirection=cVoaDirection, cVoaEntry=cVoaEntry, cVoaMIBBaseGroup=cVoaMIBBaseGroup, cVoaMIBCompliance=cVoaMIBCompliance, cVoaMIBCompliances=cVoaMIBCompliances, cVoaMIBConformance=cVoaMIBConformance, cVoaMIBGroups=cVoaMIBGroups, cVoaMIBObjects=cVoaMIBObjects, cVoaTable=cVoaTable, ciscoVoaMIB=ciscoVoaMIB)
