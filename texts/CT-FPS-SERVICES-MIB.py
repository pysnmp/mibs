#
# PySNMP MIB module CT-FPS-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FPS-SERVICES-MIB
# Produced by pysmi-1.1.12 at Tue Jun 18 01:38:33 2024
# On host fv-az1446-447 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ctFPSServices, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFPSServices")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, IpAddress, MibIdentifier, NotificationType, Gauge32, iso, Unsigned32, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32", "iso", "Unsigned32", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctFPSActivity = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1))
ctLookUpFwdActivity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctLookUpFwdActivity.setStatus('mandatory')
if mibBuilder.loadTexts: ctLookUpFwdActivity.setDescription('')
ctINBActivity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctINBActivity.setStatus('mandatory')
if mibBuilder.loadTexts: ctINBActivity.setDescription('')
mibBuilder.exportSymbols("CT-FPS-SERVICES-MIB", ctINBActivity=ctINBActivity, ctLookUpFwdActivity=ctLookUpFwdActivity, ctFPSActivity=ctFPSActivity)
