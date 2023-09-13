#
# PySNMP MIB module CTRON-WEBVIEW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-WEBVIEW-MIB
# Produced by pysmi-1.1.8 at Wed Sep 13 02:47:11 2023
# On host fv-az934-274 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ctApplication, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctApplication")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, ModuleIdentity, Counter32, iso, NotificationType, Integer32, Gauge32, TimeTicks, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "ModuleIdentity", "Counter32", "iso", "NotificationType", "Integer32", "Gauge32", "TimeTicks", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctWebView = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4))
ctEwvConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1))
ctEwvStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 2))
ctEwvDocSupport = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1))
ctEwvDocSupportAdmin = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportAdmin.setStatus('mandatory')
ctEwvDocSupportLocation = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportLocation.setStatus('mandatory')
ctEwvDocSupportAdminUID = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportAdminUID.setStatus('mandatory')
ctEwvDocSupportUsername = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportUsername.setStatus('mandatory')
ctEwvDocSupportPassword = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportPassword.setStatus('mandatory')
ctEwvSystemParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2))
ctEwvAuthScheme = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("basic", 2), ("digest", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvAuthScheme.setStatus('mandatory')
ctEwvAuthNonceValidCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvAuthNonceValidCount.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-WEBVIEW-MIB", ctEwvDocSupportLocation=ctEwvDocSupportLocation, ctEwvStatus=ctEwvStatus, ctEwvDocSupportUsername=ctEwvDocSupportUsername, ctEwvAuthNonceValidCount=ctEwvAuthNonceValidCount, ctEwvDocSupportAdminUID=ctEwvDocSupportAdminUID, ctEwvSystemParameters=ctEwvSystemParameters, ctEwvAuthScheme=ctEwvAuthScheme, ctEwvDocSupportAdmin=ctEwvDocSupportAdmin, ctEwvDocSupportPassword=ctEwvDocSupportPassword, ctEwvDocSupport=ctEwvDocSupport, ctWebView=ctWebView, ctEwvConfiguration=ctEwvConfiguration)
