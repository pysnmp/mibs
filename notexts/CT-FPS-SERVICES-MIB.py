#
# PySNMP MIB module CT-FPS-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FPS-SERVICES-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 17:11:53 2021
# On host fv-az33-471 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ctFPSServices, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFPSServices")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, IpAddress, Bits, Gauge32, MibIdentifier, ObjectIdentity, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "ObjectIdentity", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctFPSActivity = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1))
ctLookUpFwdActivity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctLookUpFwdActivity.setStatus('mandatory')
ctINBActivity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctINBActivity.setStatus('mandatory')
mibBuilder.exportSymbols("CT-FPS-SERVICES-MIB", ctLookUpFwdActivity=ctLookUpFwdActivity, ctFPSActivity=ctFPSActivity, ctINBActivity=ctINBActivity)
