#
# PySNMP MIB module CISCO-DMN-DSG-FPUI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DMN-DSG-FPUI-MIB
# Source digest sha256:300c04580c643490677b2e4fefe82cb919602eba3c8a500224ec199b3836f701
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGFPUI = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24))
ciscoDSGFPUI.setRevisions(('2010-08-30 11:00', '2010-03-22 05:00', '2009-12-20 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGFPUI.setRevisionsDescriptions(('V01.00.02 2010-08-30\n                   Updated for adherence to SNMPv2 format.', 'V01.00.01 2010-03-22\n                    The Syntax of Unsigned32 MIB objects whose range\n                    is within the range of Integer32, is updated to\n                    Integer32.', 'V01.00.00 2009-12-20\n                    Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGFPUI.setLastUpdated('2010-08-30 11:00')
if mibBuilder.loadTexts: ciscoDSGFPUI.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGFPUI.setContactInfo('Cisco Systems, Inc.\n        Customer Service\n        Postal: 170 W Tasman Drive\n        San Jose, CA 95134\n        USA\n        Tel: +1 800 553 NETS\n\n        E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGFPUI.setDescription('Cisco Front Panel User Interface MIB.')
fpuiKBLock = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiKBLock.setStatus('current')
if mibBuilder.loadTexts: fpuiKBLock.setDescription('Controls the keyboard lock.')
fpuiKBLockTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiKBLockTimeout.setStatus('current')
if mibBuilder.loadTexts: fpuiKBLockTimeout.setDescription('Keyboard lock timeout.')
fpuiLCDContrast = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiLCDContrast.setStatus('current')
if mibBuilder.loadTexts: fpuiLCDContrast.setDescription('LCD contrast setting.')
fpuiAWReminder = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiAWReminder.setStatus('current')
if mibBuilder.loadTexts: fpuiAWReminder.setDescription('Enable/Disable flashing alarms and warnings on front panel.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-FPUI-MIB", PYSNMP_MODULE_ID=ciscoDSGFPUI, ciscoDSGFPUI=ciscoDSGFPUI, fpuiAWReminder=fpuiAWReminder, fpuiKBLock=fpuiKBLock, fpuiKBLockTimeout=fpuiKBLockTimeout, fpuiLCDContrast=fpuiLCDContrast)
