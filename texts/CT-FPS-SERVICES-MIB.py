#
# PySNMP MIB module CT-FPS-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FPS-SERVICES-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 09:11:10 2024
# On host fv-az2021-432 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ctFPSServices, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFPSServices")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, Gauge32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, TimeTicks, ModuleIdentity, Bits, Counter32, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Gauge32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Bits", "Counter32", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctFPSActivity = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1))
ctLookUpFwdActivity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctLookUpFwdActivity.setStatus('mandatory')
if mibBuilder.loadTexts: ctLookUpFwdActivity.setDescription('')
ctINBActivity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctINBActivity.setStatus('mandatory')
if mibBuilder.loadTexts: ctINBActivity.setDescription('')
mibBuilder.exportSymbols("CT-FPS-SERVICES-MIB", ctFPSActivity=ctFPSActivity, ctINBActivity=ctINBActivity, ctLookUpFwdActivity=ctLookUpFwdActivity)
