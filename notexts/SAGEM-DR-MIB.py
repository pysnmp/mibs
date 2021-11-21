#
# PySNMP MIB module SAGEM-DR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/SAGEM-DR-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 13:24:17 2021
# On host fv-az74-779 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, Gauge32, ObjectIdentity, iso, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, TimeTicks, Bits, NotificationType, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Gauge32", "ObjectIdentity", "iso", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "TimeTicks", "Bits", "NotificationType", "IpAddress", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sagemDr = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038))
if mibBuilder.loadTexts: sagemDr.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: sagemDr.setOrganization('SAGEM-Tolbiac')
mibBuilder.exportSymbols("SAGEM-DR-MIB", sagemDr=sagemDr, PYSNMP_MODULE_ID=sagemDr)
