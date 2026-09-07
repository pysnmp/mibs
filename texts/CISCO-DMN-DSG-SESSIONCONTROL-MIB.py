#
# PySNMP MIB module CISCO-DMN-DSG-SESSIONCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DMN-DSG-SESSIONCONTROL-MIB
# Source digest sha256:92f9b34277a0c7551c356fe65c5ffae5440ecfe832cc6395e5d1ed87565a89f0
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGSessionControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6))
ciscoDSGSessionControl.setRevisions(('2010-08-30 11:00', '2009-11-22 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGSessionControl.setRevisionsDescriptions(('V01.00.01 2010-08-30\n                    Updated for adherence to SNMPv2 format.', 'V01.00.00 2009-11-22\n                    Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGSessionControl.setLastUpdated('2010-08-30 11:00')
if mibBuilder.loadTexts: ciscoDSGSessionControl.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGSessionControl.setContactInfo('Cisco Systems, Inc.\n        Customer Service \n        Postal: 170 W Tasman Drive\n        San Jose, CA 95134\n        USA  \n        Tel: +1 800 553 NETS\n        \n        E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGSessionControl.setDescription('Cisco DSG Session Control MIB.')
sessionControlOpen = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("open", 1), ("writeOnly", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sessionControlOpen.setStatus('current')
if mibBuilder.loadTexts: sessionControlOpen.setDescription('Open the session. 1 indicates OPEN.')
sessionControlClose = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("saveAndClose", 1), ("ignoreAndClose", 2), ("writeOnly", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sessionControlClose.setStatus('current')
if mibBuilder.loadTexts: sessionControlClose.setDescription('Close the session.')
sessionControlStatus = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("open", 1), ("closed", 2), ("expired", 3), ("openWithInvalidConfig", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionControlStatus.setStatus('current')
if mibBuilder.loadTexts: sessionControlStatus.setDescription('Status of the last opened session.')
sessionControlValidateStatus = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionControlValidateStatus.setStatus('current')
if mibBuilder.loadTexts: sessionControlValidateStatus.setDescription('If the sessioncontrolstatus object displays invalid\n          configuration, this object displays the reason for\n          invalidity.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-SESSIONCONTROL-MIB", PYSNMP_MODULE_ID=ciscoDSGSessionControl, ciscoDSGSessionControl=ciscoDSGSessionControl, sessionControlClose=sessionControlClose, sessionControlOpen=sessionControlOpen, sessionControlStatus=sessionControlStatus, sessionControlValidateStatus=sessionControlValidateStatus)
