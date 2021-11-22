#
# PySNMP MIB module SAGEM-DR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/SAGEM-DR-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:30:21 2021
# On host fv-az83-627 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, Bits, iso, Counter32, NotificationType, Integer32, enterprises, TimeTicks, Unsigned32, Counter64, Gauge32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Bits", "iso", "Counter32", "NotificationType", "Integer32", "enterprises", "TimeTicks", "Unsigned32", "Counter64", "Gauge32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sagemDr = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038))
if mibBuilder.loadTexts: sagemDr.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: sagemDr.setOrganization('SAGEM-Tolbiac')
mibBuilder.exportSymbols("SAGEM-DR-MIB", sagemDr=sagemDr, PYSNMP_MODULE_ID=sagemDr)
