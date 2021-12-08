#
# PySNMP MIB module CT-FPS-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FPS-SERVICES-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 20:26:37 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ctFPSServices, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFPSServices")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Counter32, NotificationType, Counter64, Unsigned32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Bits, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Counter32", "NotificationType", "Counter64", "Unsigned32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Bits", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctFPSActivity = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1))
ctLookUpFwdActivity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctLookUpFwdActivity.setStatus('mandatory')
ctINBActivity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctINBActivity.setStatus('mandatory')
mibBuilder.exportSymbols("CT-FPS-SERVICES-MIB", ctLookUpFwdActivity=ctLookUpFwdActivity, ctINBActivity=ctINBActivity, ctFPSActivity=ctFPSActivity)
