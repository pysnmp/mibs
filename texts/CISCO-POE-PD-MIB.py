#
# PySNMP MIB module CISCO-POE-PD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-POE-PD-MIB
# Source digest sha256:eae4d27a3dbe0d1ffd0b60dda69b19d82edd419e5aafea8239ef36e9d3af36c6
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPoePdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 414))
ciscoPoePdMIB.setRevisions(('2004-05-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPoePdMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPoePdMIB.setLastUpdated('2004-05-05 00:00')
if mibBuilder.loadTexts: ciscoPoePdMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoPoePdMIB.setContactInfo('        Cisco Systems,\n                        Customer Service\n                        Postal: 170 West Tasman Drive\n\t\t\tSan Jose, CA  95134\n\t\t\tUSA\n                        Tel: +1 800 553-NETS                 \n            \n                E-mail: cs-poe@cisco.com')
if mibBuilder.loadTexts: ciscoPoePdMIB.setDescription('This MIB is intended for devices powered by \n                external power sources, in particular Power \n                Over Ethernet (PoE or formerly called inline \n                power), to provide power usage configuration \n                and information for NMS.  For example, PoE \n                supplies DC power over standard Category 5 \n                unshielded twisted-pair (UTP) cable.  Instead \n                of requiring wall power, powered devices such \n                as IP telephones can utilize power provided\n                from power source equipments.  By using Cisco\n                Discovery Protocol (CDP),  powered devices \n                can negotiated with power source equipment to\n                obtain optimum power supply. \n                  \n                 \n                                  GLOSSARY\n\n                Midspan Injector\n                    The midspan PSE sends out a signal tone down\n                    one of the unused pairs of the standard \n                    Category 5 cable and detects tone on the \n                    other unused pair when the PD loops this tone\n                    back to it through a loopback transformer.  \n                    Once the midspan PSE detects this tone, it \n                    begins to provide power down the cable using \n                    the unused pairs.  The midspan PSE provide no \n                    physical layer capability. \n\n                Powered Device ( PD )\n                    These are devices powered by external electrical\n                    power sources.  They are, for example, IP \n                    telephones and wireless Access Points or bridges. \n\n                Power Source Equipment ( PSE )\n                    These are devices supplying electrical power to  \n                    other equipments.  They are, for example, inline \n                    power switches and power patch panels.')
cpoePdMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 0))
cpoePdMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 1))
cpoePdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2))
cpoePdInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1))
class CpoePdPowerSourceType(TextualConvention, Integer32):
    description = 'This is the type of power source equipment supplying\n                DC power to the PD.\n                    pending   -- power source is not yet determined.\n                    acAdaptor -- power is supplied by an AC adapter\n                    thirdParty  -- power is supplied by a PSE not \n                                   supporting Cisco CDP \n                    classic   -- power is supplied and limited by \n                                 a classic Cisco PSE\n                    midspan   -- power is supplied by a midspan \n                                 injector\n                    cdpNegotiated  -- power is negotiated using Cisco\n                                      CDP\n                    highPowerClassic -- power is supplied by Cisco\n                                        PSE without negotiation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("pending", 1), ("acAdaptor", 2), ("thirdParty", 3), ("classic", 4), ("midspan", 5), ("cdpNegotiated", 6), ("highPowerClassic", 7))

cpoePdCurrentPowerLevel = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdCurrentPowerLevel.setStatus('current')
if mibBuilder.loadTexts: cpoePdCurrentPowerLevel.setDescription('This identifies the currently how much power \n                is consummed by the device at which this agent\n                is running.  The level shall be one of the\n                cpoePdSupportedPowerLevel in the  \n                cpoePdSupportedPowerTable.')
cpoePdCurrentPowerSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 2), CpoePdPowerSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdCurrentPowerSource.setStatus('current')
if mibBuilder.loadTexts: cpoePdCurrentPowerSource.setDescription('This is the current power source type \n                obtained from device power source detection.')
cpoePdSupportedPowerLevelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelTable.setStatus('current')
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelTable.setDescription('This table shows all the supported electrical\n                power consumption levels of this agent and the\n                corresponding modes of operation at those power\n                levels.  The mode of operation and the device \n                capability changes as the supplied power level\n                varies.  The number of supported levels is \n                platform and implementation dependent.')
cpoePdSupportedPowerLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-POE-PD-MIB", "cpoePdSupportedPowerLevel"))
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelEntry.setStatus('current')
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelEntry.setDescription('Each entry shows a supported power level \n                and the corresponding mode of operation.')
cpoePdSupportedPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpoePdSupportedPowerLevel.setStatus('current')
if mibBuilder.loadTexts: cpoePdSupportedPowerLevel.setDescription('This index uniquely identifies the supported \n                power consumption level.')
cpoePdSupportedPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdSupportedPower.setStatus('current')
if mibBuilder.loadTexts: cpoePdSupportedPower.setDescription('This is the electrical power consummed by\n                the device operating at this supported power\n                consumption level.')
cpoePdSupportedPowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdSupportedPowerMode.setStatus('current')
if mibBuilder.loadTexts: cpoePdSupportedPowerMode.setDescription("This is a text string describing the mode of\n                operation or capability of the device at the\n                power consumption level.  For example, the \n                comsumption level and corresponding mode should\n                look like these:\n                    1  'Full power mode'\n                    2  'Low power mode - dot11radio 0 disabled'\n                    3  'Low power mode - dot11radio 1 disabled'\n                    4  'Low power mode - dot11 radios disabled'.")
cpoePdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1))
cpoePdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2))
cpoePdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1, 1)).setObjects(("CISCO-POE-PD-MIB", "cpoePdInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpoePdMIBCompliance = cpoePdMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cpoePdMIBCompliance.setDescription('The compliance statement for the SNMP entities that\n                 implement the ciscoPoePdMIB module.')
cpoePdInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2, 1)).setObjects(("CISCO-POE-PD-MIB", "cpoePdCurrentPowerLevel"), ("CISCO-POE-PD-MIB", "cpoePdCurrentPowerSource"), ("CISCO-POE-PD-MIB", "cpoePdSupportedPower"), ("CISCO-POE-PD-MIB", "cpoePdSupportedPowerMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpoePdInformationGroup = cpoePdInformationGroup.setStatus('current')
if mibBuilder.loadTexts: cpoePdInformationGroup.setDescription('This collection of objects provide information about\n                the supported electrical power level, current power\n                consumption, and mode of operation of this agent.')
mibBuilder.exportSymbols("CISCO-POE-PD-MIB", CpoePdPowerSourceType=CpoePdPowerSourceType, PYSNMP_MODULE_ID=ciscoPoePdMIB, ciscoPoePdMIB=ciscoPoePdMIB, cpoePdCurrentPowerLevel=cpoePdCurrentPowerLevel, cpoePdCurrentPowerSource=cpoePdCurrentPowerSource, cpoePdInformation=cpoePdInformation, cpoePdInformationGroup=cpoePdInformationGroup, cpoePdMIBCompliance=cpoePdMIBCompliance, cpoePdMIBCompliances=cpoePdMIBCompliances, cpoePdMIBConformance=cpoePdMIBConformance, cpoePdMIBGroups=cpoePdMIBGroups, cpoePdMIBNotifications=cpoePdMIBNotifications, cpoePdMIBObjects=cpoePdMIBObjects, cpoePdSupportedPower=cpoePdSupportedPower, cpoePdSupportedPowerLevel=cpoePdSupportedPowerLevel, cpoePdSupportedPowerLevelEntry=cpoePdSupportedPowerLevelEntry, cpoePdSupportedPowerLevelTable=cpoePdSupportedPowerLevelTable, cpoePdSupportedPowerMode=cpoePdSupportedPowerMode)
