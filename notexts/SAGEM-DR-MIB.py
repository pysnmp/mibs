#
# PySNMP MIB module SAGEM-DR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/SAGEM-DR-MIB
# Produced by pysmi-1.1.3 at Thu Dec  9 15:36:06 2021
# On host fv-az83-649 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter64, Bits, TimeTicks, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Counter32, NotificationType, MibIdentifier, Integer32, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Bits", "TimeTicks", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Counter32", "NotificationType", "MibIdentifier", "Integer32", "Unsigned32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sagemDr = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038))
if mibBuilder.loadTexts: sagemDr.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: sagemDr.setOrganization('SAGEM-Tolbiac')
mibBuilder.exportSymbols("SAGEM-DR-MIB", sagemDr=sagemDr, PYSNMP_MODULE_ID=sagemDr)
